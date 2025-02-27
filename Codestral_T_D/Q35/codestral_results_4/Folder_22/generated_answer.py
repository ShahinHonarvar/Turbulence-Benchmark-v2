def remove_repeat_chars(s):
    chars_to_remove = {char for char in s[50:200] if s[50:200].count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))