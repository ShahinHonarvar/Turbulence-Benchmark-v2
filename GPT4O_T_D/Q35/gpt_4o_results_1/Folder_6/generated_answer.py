def remove_repeat_chars(s):
    section = s[21:93]
    char_count = {}
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) <= 20 or s.index(char) >= 93))
    return result