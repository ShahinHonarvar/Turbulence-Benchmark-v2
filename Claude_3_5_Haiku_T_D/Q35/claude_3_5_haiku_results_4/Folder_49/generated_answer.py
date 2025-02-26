def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    substr = s[91:200]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) < 91 or s.index(char) > 200))