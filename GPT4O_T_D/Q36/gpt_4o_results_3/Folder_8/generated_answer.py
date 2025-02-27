def filter_chars(s):
    result = s[:83]
    exclude = set()
    for i in range(83, 93):
        if '!' < s[i] < '*':
            exclude.add(s[i])
    result += ''.join((c for c in s[93:] if c not in exclude))
    return result