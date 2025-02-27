def remove_repeat_chars(input_string):
    chars_to_remove = set(input_string[330:543])
    chars_to_remove = {ch for ch in chars_to_remove if input_string[330:543].count(ch) > 1}
    return ''.join((c for c in input_string if c not in chars_to_remove))