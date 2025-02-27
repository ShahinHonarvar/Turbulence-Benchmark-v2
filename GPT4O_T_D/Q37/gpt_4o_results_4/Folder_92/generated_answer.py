def filter_chars(s):
    if len(s) > 4:
        target_chars = [c for c in s[4:5] if '7' <= c <= 'o']
        for char in target_chars:
            s = s.replace(char, '')
    return s