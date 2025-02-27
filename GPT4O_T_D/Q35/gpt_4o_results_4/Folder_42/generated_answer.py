def remove_repeat_chars(s):
    check_range = s[19:60]
    to_remove = {char for char in check_range if check_range.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove or not 19 <= s.index(char) < 60))