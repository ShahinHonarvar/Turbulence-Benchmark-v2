def remove_repeat_chars(s):
    target_slice = s[91:97]
    char_counts = {}
    for char in target_slice:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))