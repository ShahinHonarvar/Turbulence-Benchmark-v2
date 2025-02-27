def remove_repeat_chars(s):
    char_count = {}
    for char in s[57:84]:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    chars_to_remove = [char for char, count in char_count.items() if count > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s