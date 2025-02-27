def remove_repeat_chars(s):
    sub_str = s[11:76]
    char_count = {char: sub_str.count(char) for char in set(sub_str) if sub_str.count(char) > 1}
    result = ''.join((char for char in s if char not in char_count or not 11 < s.index(char) < 76))
    return result