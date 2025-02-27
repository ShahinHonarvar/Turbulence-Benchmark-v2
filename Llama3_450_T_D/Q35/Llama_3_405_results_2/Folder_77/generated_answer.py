def remove_repeat_chars(s):
    chars_to_remove = set()
    char_counts = {}
    for i in range(355, 988):
        if i < len(s):
            char = s[i]
            char_counts[char] = char_counts.get(char, 0) + 1
            if char_counts[char] > 1:
                chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])