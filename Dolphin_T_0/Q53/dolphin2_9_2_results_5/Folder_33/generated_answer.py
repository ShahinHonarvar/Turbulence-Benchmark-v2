def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for sub_s in range(len(s)):
        for length in range(141, len(s) - sub_s + 1):
            substr = s[sub_s:sub_s + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result