def filter_chars(s):
    s_list = list(s)
    chars_to_remove = set(s_list[91:97])
    chars_to_remove = {c for c in chars_to_remove if 'j' < c < 'w'}
    s_list = [c for c in s_list if c not in chars_to_remove]
    return ''.join(s_list)