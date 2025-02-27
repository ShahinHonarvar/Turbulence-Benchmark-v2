def remove_repeat_chars(s):
    to_remove = {char for char in s[86:89] if s[86:89].count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))