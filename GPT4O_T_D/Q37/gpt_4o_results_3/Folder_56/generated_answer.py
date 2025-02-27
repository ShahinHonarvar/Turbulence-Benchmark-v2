def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 71:
        end_index = min(95, len(s))
        for char in s[71:end_index]:
            if 'K' <= char <= 'a':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))