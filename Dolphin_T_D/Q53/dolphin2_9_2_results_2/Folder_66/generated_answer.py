def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for length in range(76, 0, -1):
        for i in range(n - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result