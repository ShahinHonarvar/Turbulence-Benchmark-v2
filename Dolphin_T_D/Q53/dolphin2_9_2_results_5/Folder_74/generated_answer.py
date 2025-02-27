def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 57, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result