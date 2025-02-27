def remove_repeat_chars(s):
    char_count = {}
    chars_to_remove = set()
    for i in range(33, 78):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
                chars_to_remove.add(char)
            else:
                char_count[char] = 1
    return ''.join([char for char in s if char not in chars_to_remove])