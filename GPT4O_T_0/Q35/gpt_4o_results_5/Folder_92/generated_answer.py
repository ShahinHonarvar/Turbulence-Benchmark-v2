def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    middle_section = s[1:2]
    char_count = {}
    for char in middle_section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))