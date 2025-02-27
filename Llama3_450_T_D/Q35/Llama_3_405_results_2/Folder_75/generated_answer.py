def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for i in range(20, 51):
        if i < len(s):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])