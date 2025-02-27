def remove_repeat_chars(s):
    substring = s[3:7]
    char_counts = {char: substring.count(char) for char in substring}
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))