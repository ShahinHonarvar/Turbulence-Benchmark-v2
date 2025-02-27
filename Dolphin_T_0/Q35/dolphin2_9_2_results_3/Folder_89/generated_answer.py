def remove_repeat_chars(s):
    chars = list(s)
    chars_between_55_and_84 = chars[55:84]
    chars_to_remove = []
    for char in chars_between_55_and_84:
        if chars_between_55_and_84.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.append(char)
            s = s.replace(char, '')
    return s