def remove_repeat_chars(input_string):
    substring = input_string[57:88]
    repeat_chars = {c for c in substring if substring.count(c) > 1}
    return ''.join((c for c in input_string if c not in repeat_chars))