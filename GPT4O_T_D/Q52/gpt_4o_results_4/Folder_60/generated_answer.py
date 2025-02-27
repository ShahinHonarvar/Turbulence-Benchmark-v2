def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    target_length = 88
    for i in range(n - target_length + 1):
        substr = s[i:i + target_length]
        if substr == substr[::-1]:
            result.add(substr)
    return result