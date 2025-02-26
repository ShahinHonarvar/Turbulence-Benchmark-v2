def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    substring = s[4:8]
    chars_to_remove = set((char for char in substring if substring.count(char) > 1))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result