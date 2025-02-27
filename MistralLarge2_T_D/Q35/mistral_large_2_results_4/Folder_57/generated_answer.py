def remove_repeat_chars(s):
    substring = s[25:80]
    repeat_chars = {char for char in substring if substring.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result