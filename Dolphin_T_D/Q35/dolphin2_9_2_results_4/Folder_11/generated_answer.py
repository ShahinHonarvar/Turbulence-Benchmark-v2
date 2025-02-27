def remove_repeat_chars(s):
    chars = [char for char in s if 48 < ord(char) < 76]
    char_counts = {char: chars.count(char) for char in chars}
    remove_chars = [char for char, count in char_counts.items() if count > 1]
    for char in remove_chars:
        s = s.replace(char, '')
    return s