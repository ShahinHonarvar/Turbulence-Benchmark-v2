def remove_repeat_chars(s):
    if len(s) <= 250:
        return s
    segment = s[51:200]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 51 or s.index(char) >= 200))