def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    mid_section = s[21:200]
    char_count = {}
    for char in mid_section:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result