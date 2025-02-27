def remove_repeat_chars(s):
    char_count = {}
    for char in s[355:988]:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))