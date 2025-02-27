def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 33):
        for j in range(i + 33, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) >= 34:
                result.add(substring)
    return result