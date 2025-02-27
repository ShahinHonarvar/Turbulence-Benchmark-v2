def palindrome_of_length_n(s):
    n = 84
    normalized_s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(len(normalized_s) - n + 1):
        substr = normalized_s[i:i + n]
        if substr == substr[::-1]:
            result.add(substr)
    return result