def remove_repeat_chars(s):
    if len(s) <= 31:
        return s
    sub_string = s[31:200]
    char_count = {}
    for char in sub_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 30 or s.index(char) >= 200))