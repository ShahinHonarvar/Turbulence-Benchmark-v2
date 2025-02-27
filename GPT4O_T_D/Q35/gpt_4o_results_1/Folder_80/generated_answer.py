def remove_repeat_chars(s):
    target_range = s[58:84]
    char_count = {char: target_range.count(char) for char in set(target_range)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 58 <= s.index(char) < 84))