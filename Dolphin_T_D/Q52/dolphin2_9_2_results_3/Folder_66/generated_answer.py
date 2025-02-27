def palindrome_of_length_n(s):
    s = s.lower()
    set_palindrome = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if substring == substring[::-1]:
            set_palindrome.add(substring)
    return set_palindrome