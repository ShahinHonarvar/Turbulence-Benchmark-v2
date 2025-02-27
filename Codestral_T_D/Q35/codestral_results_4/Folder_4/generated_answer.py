def remove_repeat_chars(s):
    chars = s[49:74]
    counts = {char: chars.count(char) for char in chars}
    repeat_chars = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))