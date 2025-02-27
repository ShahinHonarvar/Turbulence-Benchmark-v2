def palindrome_of_length_n(s):
    result = set()
    normalized_s = ''.join(filter(str.isalpha, s)).lower()
    str_len = len(normalized_s)
    for i in range(str_len - 46):
        substr = normalized_s[i:i + 47]
        if substr == substr[::-1]:
            result.add(substr)
    return result