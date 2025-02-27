def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(s) - 28):
        substr = s[i:i + 29]
        if substr == substr[::-1]:
            result.add(substr)
    return result