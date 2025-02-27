def remove_repeat_chars(s):
    sub_str = s[81:86]
    char_count = {char: sub_str.count(char) for char in sub_str}
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    return ''.join((char for char in s if char not in repeat_chars))