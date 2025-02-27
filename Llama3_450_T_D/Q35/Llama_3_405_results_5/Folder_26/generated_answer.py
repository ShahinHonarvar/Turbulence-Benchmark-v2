def remove_repeat_chars(s):
    char_count = {}
    for i in range(68, 99):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = set([char for char, count in char_count.items() if count > 1])
    return ''.join([c for c in s if c not in chars_to_remove])