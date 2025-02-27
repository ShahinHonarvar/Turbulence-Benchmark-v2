def remove_repeat_chars(s):
    if len(s) <= 5:
        return s
    substring = s[1:5]
    repeating_chars = {char for char in substring if substring.count(char) > 1}
    result = ''.join((char for char in s if char not in repeating_chars))
    return result