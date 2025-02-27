def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(len(s)) if 69 < i < 97 and 'V' < s[i] < 'j'))
    return ''.join((c for c in s if c not in chars_to_remove))