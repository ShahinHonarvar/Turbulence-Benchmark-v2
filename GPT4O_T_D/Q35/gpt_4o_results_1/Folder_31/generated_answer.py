def remove_repeat_chars(s):
    target_section = s[34:78]
    char_count = {}
    for char in target_section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 33 or s.index(char) >= 78))
    return result