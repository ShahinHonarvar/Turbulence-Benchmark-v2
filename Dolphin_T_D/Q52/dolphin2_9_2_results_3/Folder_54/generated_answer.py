def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result