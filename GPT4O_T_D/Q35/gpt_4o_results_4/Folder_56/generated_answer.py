def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    sub_string = s[8:9]
    char_counts = {char: sub_string.count(char) for char in set(sub_string)}
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))