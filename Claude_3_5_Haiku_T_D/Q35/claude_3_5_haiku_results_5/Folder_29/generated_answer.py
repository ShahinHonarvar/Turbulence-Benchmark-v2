def remove_repeat_chars(s):
    char_counts = {}
    for i in range(71, 98):
        if 0 <= i < len(s):
            char = s[i]
            char_counts[char] = char_counts.get(char, 0) + 1
    remove_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in remove_chars))