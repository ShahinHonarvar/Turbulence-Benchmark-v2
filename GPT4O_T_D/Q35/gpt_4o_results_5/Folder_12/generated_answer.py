def remove_repeat_chars(s):
    if len(s) <= 16:
        return s
    char_map = {}
    for i in range(17, min(87, len(s))):
        char = s[i]
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    to_remove = {char for char, count in char_map.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove or s.index(char) <= 16 or s.index(char) >= 87))