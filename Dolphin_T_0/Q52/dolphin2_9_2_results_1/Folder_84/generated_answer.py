def palindrome_of_length_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s) - 130):
        substring = s[i:i + 131]
        if substring == substring[::-1]:
            set_of_palindromes.add(substring)
    return set_of_palindromes