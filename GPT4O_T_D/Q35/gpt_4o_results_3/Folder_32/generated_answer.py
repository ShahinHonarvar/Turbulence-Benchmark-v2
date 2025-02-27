def remove_repeat_chars(s):
    sub_string = s[87:90]
    repeated_chars = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))