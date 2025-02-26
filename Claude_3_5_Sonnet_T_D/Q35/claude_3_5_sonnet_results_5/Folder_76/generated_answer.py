def remove_repeat_chars(s):
    char_count = {}
    for i in range(331, 543):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in s if char not in chars_to_remove))