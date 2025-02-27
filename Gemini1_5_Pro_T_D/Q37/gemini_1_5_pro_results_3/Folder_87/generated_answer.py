def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i in range(18, 82) and 'W' <= s[i] <= '[':
            if s[i] not in result:
                result += s[i]
        else:
            result += s[i]
    return result