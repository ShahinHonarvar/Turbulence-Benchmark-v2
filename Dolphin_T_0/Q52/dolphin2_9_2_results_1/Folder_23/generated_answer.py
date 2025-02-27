def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 68):
        substr = s[i:i + 69]
        if substr == substr[::-1]:
            result.add(substr)
    return result