def filter_chars(s):
    result = []
    for i in range(len(s)):
        if 13 <= i <= 28 and 'c' <= s[i] <= 'n':
            continue
        result.append(s[i])
    return ''.join(result)