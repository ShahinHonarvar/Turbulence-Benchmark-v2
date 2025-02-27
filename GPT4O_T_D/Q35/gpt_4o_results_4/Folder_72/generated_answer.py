def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    substring = s[14:70]
    chars_to_remove = {char for char in substring if substring.count(char) > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 13 or s.index(char) >= 70))
    return result