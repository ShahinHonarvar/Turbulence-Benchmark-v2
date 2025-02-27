def remove_repeat_chars(s):
    chars_to_remove = set([c for c in s[55:84] if s.count(c) > 1])
    output_string = ''
    for char in s:
        if char not in chars_to_remove:
            output_string += char
    return output_string