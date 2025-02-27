def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    sub_s = s[12:76]
    char_count = {}
    for char in sub_s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars or (s.index(char) <= 11 or s.index(char) >= 76)))