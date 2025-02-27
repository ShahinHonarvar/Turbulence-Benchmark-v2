def filter_chars(s: str) -> str:
    chars_to_remove = set(s[299:418])
    chars_to_remove = {char for char in chars_to_remove if '9' < char < 'P'}
    s_list = list(s)
    for i, char in enumerate(s_list):
        if char in chars_to_remove:
            s_list[i] = ''
    return ''.join(s_list)