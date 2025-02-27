def remove_repeat_chars(s):
    char_counts = {}
    for i in range(36, 85):
        if i < len(s):
            char = s[i]
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join([char for char in s if char not in chars_to_remove])