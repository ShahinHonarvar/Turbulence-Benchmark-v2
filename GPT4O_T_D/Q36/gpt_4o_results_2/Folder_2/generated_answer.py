def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('D') + 1, ord('J'))}
    part_to_check = s[422:854]
    chars_to_remove = {c for c in part_to_check if c in to_remove}
    return ''.join((c for c in s if c not in chars_to_remove))