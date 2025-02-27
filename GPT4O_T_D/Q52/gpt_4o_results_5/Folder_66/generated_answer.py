def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 25
    result = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            result.add(substr)
    return result