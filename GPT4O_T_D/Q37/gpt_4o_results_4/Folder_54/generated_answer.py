def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 46:
        end_index = min(len(s), 86)
        for char in s[46:end_index]:
            if '-' <= char <= 'X':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))