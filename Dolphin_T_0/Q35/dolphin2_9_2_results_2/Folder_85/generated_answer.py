def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[1:8] if s.count(c) > 1]
    new_string = ''
    for c in s:
        if c not in chars_to_remove:
            new_string += c
    return new_string