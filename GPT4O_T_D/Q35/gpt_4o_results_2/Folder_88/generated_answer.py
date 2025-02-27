def remove_repeat_chars(s):
    substring = s[4:9]
    counted_chars = {char for char in substring if substring.count(char) > 1}
    return ''.join((char for char in s if char not in counted_chars or not 4 <= s.index(char) < 9))