def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result