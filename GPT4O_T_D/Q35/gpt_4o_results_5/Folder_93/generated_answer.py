def remove_repeat_chars(s):
    if len(s) <= 57:
        return s
    char_count = {}
    for char in s[58:85]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for i, char in enumerate(s) if char not in chars_to_remove or i <= 57 or i >= 85))