def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(0, len(s) - 47):
        substring = s[i:i + 48]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result