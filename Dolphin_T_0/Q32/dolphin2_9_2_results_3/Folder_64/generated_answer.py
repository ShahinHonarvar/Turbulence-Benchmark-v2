def insert_after_character(s):
    return 'u'.join(('ud' if c == 'u' else c for c in s))