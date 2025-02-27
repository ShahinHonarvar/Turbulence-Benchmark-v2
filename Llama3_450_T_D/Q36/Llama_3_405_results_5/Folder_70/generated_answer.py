def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(170, len(s)) if i < 195 and '!' < s[i] < '}'))
    return ''.join((c for c in s if c not in chars_to_remove))