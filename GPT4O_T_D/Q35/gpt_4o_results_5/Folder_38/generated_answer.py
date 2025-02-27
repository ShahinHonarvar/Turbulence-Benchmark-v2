def remove_repeat_chars(s):
    sub_string = s[37:85]
    char_count = {char: sub_string.count(char) for char in set(sub_string)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 36 or s.index(char) >= 85))