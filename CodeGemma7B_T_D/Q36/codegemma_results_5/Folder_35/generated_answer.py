def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(164, 658)])
    filtered_str = ''
    for c in s:
        if c not in chars_to_remove or c not in filtered_str:
            filtered_str += c
    return filtered_str