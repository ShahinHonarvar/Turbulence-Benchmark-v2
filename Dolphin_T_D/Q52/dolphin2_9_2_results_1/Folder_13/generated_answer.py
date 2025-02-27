def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 205):
        substr = s[i:i + 206]
        if substr == substr[::-1]:
            result.add(substr)
    return result