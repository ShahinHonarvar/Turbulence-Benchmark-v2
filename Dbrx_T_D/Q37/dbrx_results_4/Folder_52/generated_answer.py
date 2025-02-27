def filter_chars(s):
    for i in range(len(s)):
        if 54 <= i <= 83 and s[i] >= 'j' and (s[i] <= 'v'):
            s = s[:i] + s[i + 1:]
            i -= 1
    return s