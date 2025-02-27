def filter_chars(s):
    filtered_chars = [c for c in s if 11 <= s.index(c) <= 32 and ord('!') <= ord(c) <= ord('@')]
    return ''.join([c for i, c in enumerate(s) if i not in filtered_chars])