def remove_repeat_chars(s):
    to_remove = {char for char in s[20:36] if s[20:36].count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))