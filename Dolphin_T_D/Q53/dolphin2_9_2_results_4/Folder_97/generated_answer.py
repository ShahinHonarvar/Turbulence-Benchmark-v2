def palindrome_of_length_at_least_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    for length in range(138, len(s) + 1):
        for index in range(len(s) - length + 1):
            substr = s[index:index + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result