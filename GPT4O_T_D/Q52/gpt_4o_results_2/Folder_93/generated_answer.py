def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 45:
        return set()
    result = set()
    for i in range(len(s) - 44):
        substr = s[i:i + 45]
        if substr == substr[::-1]:
            result.add(substr)
    return result