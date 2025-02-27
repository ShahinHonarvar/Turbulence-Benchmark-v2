def remove_repeat_chars(s):
    if len(s) < 97:
        return s
    substr = s[91:97]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))