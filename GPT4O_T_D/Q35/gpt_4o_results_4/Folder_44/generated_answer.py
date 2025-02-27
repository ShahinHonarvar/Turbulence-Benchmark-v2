def remove_repeat_chars(s):
    substring = s[37:52]
    char_count = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 36 or s.index(char) >= 52))