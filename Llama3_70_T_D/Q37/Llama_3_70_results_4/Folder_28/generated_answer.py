def filter_chars(s):
    chars_to_remove = set()
    for i in range(min(20, len(s)), min(80, len(s))):
        if '!' <= s[i] <= 'T':
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])