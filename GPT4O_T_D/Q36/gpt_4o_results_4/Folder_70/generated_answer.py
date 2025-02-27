def filter_chars(s):
    to_remove = set([s[i] for i in range(171, 195) if '!' < s[i] < '}'])
    return ''.join([c for c in s if c not in to_remove])