def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 81 + 1):
        for j in range(i + 81, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= 1 and len(substring) >= 81:
                result.add(substring)
    return result