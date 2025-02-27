def remove_repeat_chars(s):
    chars_to_remove = []
    for c in s[101:200]:
        if s[101:200].count(c) > 1:
            chars_to_remove.append(c)
    return ''.join((char for char in s if char not in chars_to_remove))