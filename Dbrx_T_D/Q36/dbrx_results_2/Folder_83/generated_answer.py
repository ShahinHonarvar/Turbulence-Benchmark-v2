def filter_chars(s):
    for i in range(len(s)):
        if 72 <= i < 93:
            if s[i] > '<' and s[i] < 'J':
                s = s[:i] + s[i + 1:]
    return s