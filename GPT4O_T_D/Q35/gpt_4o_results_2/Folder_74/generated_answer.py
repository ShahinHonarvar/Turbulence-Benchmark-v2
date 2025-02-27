def remove_repeat_chars(s):
    if len(s) < 98:
        return s
    sub_str = s[70:97]
    char_count = {char: sub_str.count(char) for char in set(sub_str)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 70 < s.index(char) < 97))