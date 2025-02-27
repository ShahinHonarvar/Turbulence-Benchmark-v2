def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] not in ["'", '"', 'm', 'w']:
            new_s += s[i]
    return new_s.lstrip()