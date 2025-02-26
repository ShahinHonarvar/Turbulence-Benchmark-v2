def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    segment = s[91:200]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) >= 200 or s.index(char) <= 90))