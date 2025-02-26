def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 27 <= i <= 85 and 'c' <= s[i] <= 'i':
            continue
        result += s[i]
    return result