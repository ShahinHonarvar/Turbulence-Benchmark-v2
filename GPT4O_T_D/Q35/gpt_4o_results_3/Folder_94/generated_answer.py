def remove_repeat_chars(s):
    part_to_check = s[43:87]
    chars_to_remove = {char for char in part_to_check if part_to_check.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))