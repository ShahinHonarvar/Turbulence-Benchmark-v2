def remove_repeat_chars(s):
    chars = s[44:91]
    counts = {char: chars.count(char) for char in chars}
    chars_to_remove = [char for char, count in counts.items() if count > 1]
    return ''.join((char for char in s if char not in chars_to_remove))