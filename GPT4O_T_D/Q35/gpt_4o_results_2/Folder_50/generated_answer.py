def remove_repeat_chars(s):
    substring = s[14:76]
    repeated_chars = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or char in s[:13] + s[77:]))