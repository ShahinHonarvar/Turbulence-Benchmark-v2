def remove_repeat_chars(s):
    char_counts = {}
    for char in s[69:97]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    chars_to_remove = [char for char, count in char_counts.items() if count > 1]
    return ''.join([char for char in s if char not in chars_to_remove])