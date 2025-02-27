def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 17):
        for j in range(18, min(26, len(s) - i + 1)):
            substr = s[i:i + j]
            if substr == substr[::-1]:
                result.add(substr)
    return result