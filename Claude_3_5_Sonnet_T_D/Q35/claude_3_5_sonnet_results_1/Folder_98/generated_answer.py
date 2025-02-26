def remove_repeat_chars(s):
    check_range = s[1:7]
    char_count = {char: check_range.count(char) for char in set(check_range)}
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))