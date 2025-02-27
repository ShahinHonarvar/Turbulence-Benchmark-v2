def remove_repeat_chars(s):
    mid_str = s[50:200]
    char_counts = {}
    for char in mid_str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result