def remove_repeat_chars(s):
    segment = s[51:92]
    to_remove = {c for c in segment if segment.count(c) > 1}
    return ''.join((c for c in s if c not in to_remove or s.index(c) <= 50 or s.index(c) >= 92))