def remove_repeat_chars(s):
    to_remove = [c for i, c in enumerate(s[86:90]) if s.count(c) > 1]
    result = ''.join([c for c in s if c not in to_remove])
    return result