def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length - 32):
        substr = s[i:i + 33]
        if substr == substr[::-1]:
            result.add(substr)
    return result