def filter_chars(s):
    chars_to_remove = set(s[43:69].lower()) - set('bcdefghijklmnopqrst')
    return ''.join((c for i, c in enumerate(s) if (i < 43 or i >= 69) or c.lower() not in chars_to_remove))