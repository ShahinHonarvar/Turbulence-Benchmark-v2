def filter_chars(s):
    s = list(s)
    for i in range(len(s)):
        if i >= 25 and i <= 97 and (s[i] >= 'm') and (s[i] <= 'w'):
            s = [c for c in s if c != s[i]]
    return ''.join(s)