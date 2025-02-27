def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    sub_string = s[21:35]
    char_count = {}
    for char in sub_string:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result