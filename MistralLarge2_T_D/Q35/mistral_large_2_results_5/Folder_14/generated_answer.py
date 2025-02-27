def remove_repeat_chars(s):
    to_remove = {char for char in s[2:6] if s[2:6].count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))