def remove_repeat_chars(s):
    indices_to_check = s[1:6]
    chars_to_remove = {char for char in indices_to_check if indices_to_check.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))