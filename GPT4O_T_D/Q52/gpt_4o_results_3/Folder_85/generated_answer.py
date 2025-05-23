def palindrome_of_length_n(s):
    n = 46
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            result.add(substr)
    return result