def filter_chars(s):
    filtered_chars = [c for c in s[10:79] if c > '?' and c < 'm']
    return ''.join([c for c in s if c not in filtered_chars])