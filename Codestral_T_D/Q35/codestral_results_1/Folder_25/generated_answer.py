def remove_repeat_chars(s):
    chars = s[37:43]
    counts = {char: chars.count(char) for char in chars}
    return ''.join([c for c in s if counts[c] == 1])