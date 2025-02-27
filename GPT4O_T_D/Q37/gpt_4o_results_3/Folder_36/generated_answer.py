def filter_chars(s):
    filtered_chars = {chr(i) for i in range(ord(','), ord('3') + 1)}
    exclusion_zone = set(s[259:503])
    chars_to_remove = filtered_chars.intersection(exclusion_zone)
    return ''.join((c for c in s if c not in chars_to_remove))