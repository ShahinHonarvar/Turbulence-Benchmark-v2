def remove_repeat_chars(s):
    chars_between_57_85 = s[57:85]
    repeat_chars = set([char for char in set(chars_between_57_85) if chars_between_57_85.count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])