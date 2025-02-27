def filter_chars(s):
    filtered_chars = [c for c in s if 722 <= s.index(c) <= 832 and 'K' <= c <= 'm']
    return ''.join([c for c in s if c not in filtered_chars])