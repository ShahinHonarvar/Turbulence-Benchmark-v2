def remove_repeat_chars(s):
    substring = s[20:51]
    char_count = {char: substring.count(char) for char in substring}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result