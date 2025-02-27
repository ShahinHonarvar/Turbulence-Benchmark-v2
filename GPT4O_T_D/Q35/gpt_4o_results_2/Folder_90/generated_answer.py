def remove_repeat_chars(s):
    if len(s) <= 307:
        return s
    char_count = {}
    for char in s[307:807]:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or char in s[:307] or char in s[807:]))