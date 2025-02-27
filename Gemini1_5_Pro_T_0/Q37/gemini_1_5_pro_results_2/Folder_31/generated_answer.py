def filter_chars(s):
    result = []
    for i in range(len(s)):
        c = s[i]
        if not (57 <= i <= 96 and '<' <= c <= 'w' and (c in s[:i])):
            result.append(c)
    return ''.join(result)