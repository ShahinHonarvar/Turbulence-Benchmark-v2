def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    section = s[61:200]
    char_count = {}
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove or not 61 <= s.index(char) < 200]
    return ''.join(result)