def remove_repeat_chars(s):
    repeated_chars = {char for char in s[20:51] if s[20:51].count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))