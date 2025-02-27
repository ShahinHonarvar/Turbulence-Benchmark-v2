def remove_repeat_chars(s):
    substring = s[48:76]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    return ''.join((char for char in s if char not in chars_to_remove))