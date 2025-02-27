def remove_repeat_chars(s):
    repeat_range = s[57:90]
    char_count = {}
    for char in repeat_range:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)