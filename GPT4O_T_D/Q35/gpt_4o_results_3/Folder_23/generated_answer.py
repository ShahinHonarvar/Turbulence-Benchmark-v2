def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    substring = s[21:36]
    repeat_chars = {char for char in substring if substring.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars or not 21 < s.index(char) < 36))
    return result