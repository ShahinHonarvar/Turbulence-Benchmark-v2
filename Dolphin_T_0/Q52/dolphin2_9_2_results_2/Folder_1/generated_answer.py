def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindrome_set.add(substring)
    return palindrome_set