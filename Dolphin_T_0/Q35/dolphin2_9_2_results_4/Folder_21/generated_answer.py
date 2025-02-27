def remove_repeat_chars(s):
    chars_between_indices = s[462:995]
    repeat_chars = {char for char in chars_between_indices if s.count(char) > 1}
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s