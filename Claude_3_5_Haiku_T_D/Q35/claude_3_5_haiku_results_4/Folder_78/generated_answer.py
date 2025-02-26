def remove_repeat_chars(s):
    if len(s) <= 62:
        return s
    substring = s[63:96]
    char_count = {}
    repeat_chars = set()
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 63 or s.index(char) >= 96))
    return result