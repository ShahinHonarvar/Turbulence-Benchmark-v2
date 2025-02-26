def remove_repeat_chars(s):
    check_range = s[1:5]
    char_count = {}
    for char in check_range:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars))
    return result