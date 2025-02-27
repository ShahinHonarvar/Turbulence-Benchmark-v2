def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 473):
        substr = s[i:i + 474]
        if substr.isalpha() and substr == substr[::-1]:
            result.add(substr)
    return result