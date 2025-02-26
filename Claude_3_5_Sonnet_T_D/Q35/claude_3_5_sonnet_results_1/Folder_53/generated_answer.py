def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    target_slice = s[201:202]
    char_count = {}
    for char in target_slice:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))