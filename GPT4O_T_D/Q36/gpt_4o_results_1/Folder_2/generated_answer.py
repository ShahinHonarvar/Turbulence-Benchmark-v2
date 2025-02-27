def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('E'), ord('J'))}
    for i in range(422, 854):
        if s[i] in chars_to_remove:
            s = s.replace(s[i], '')
    return s