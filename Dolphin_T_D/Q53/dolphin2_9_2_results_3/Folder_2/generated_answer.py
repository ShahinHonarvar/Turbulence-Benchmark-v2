def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for length in range(55, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result