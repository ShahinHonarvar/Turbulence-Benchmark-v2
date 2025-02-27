def remove_repeat_chars(s):
    sub_string = s[72:93]
    to_remove = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))