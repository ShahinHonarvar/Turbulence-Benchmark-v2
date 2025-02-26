def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 10 <= i <= 69 and 'I' <= s[i] <= 'K':
            continue
        result += s[i]
    return result