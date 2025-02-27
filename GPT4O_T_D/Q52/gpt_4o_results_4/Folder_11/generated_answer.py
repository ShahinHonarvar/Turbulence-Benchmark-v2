def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    result = set()
    length = 77
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            result.add(substr)
    return result