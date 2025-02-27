def remove_repeat_chars(s):
    if len(s) <= 90:
        return s
    segment = s[87:90]
    repeated_chars = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))