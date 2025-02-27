def remove_repeat_chars(s):
    section = s[57:88]
    char_count = {}
    for char in section:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))