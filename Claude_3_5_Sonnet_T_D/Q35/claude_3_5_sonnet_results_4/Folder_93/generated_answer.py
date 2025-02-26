def remove_repeat_chars(s):
    substring = s[58:85]
    char_count = {char: substring.count(char) for char in substring}
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))