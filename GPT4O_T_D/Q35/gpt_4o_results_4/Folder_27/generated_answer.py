def remove_repeat_chars(s):
    if len(s) < 89:
        return s
    substring = s[87:89]
    repeated_chars = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))