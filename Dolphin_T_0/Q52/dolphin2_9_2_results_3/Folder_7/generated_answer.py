def palindrome_of_length_n(s):
    s = s.lower()
    set_palindrome = set()
    n = 416
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            set_palindrome.add(substring)
    return set_palindrome