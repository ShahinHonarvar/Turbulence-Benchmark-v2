def remove_repeat_chars(s):
    sub_string = s[12:76]
    char_count = {}
    for char in sub_string:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 11 or s.index(char) >= 76))