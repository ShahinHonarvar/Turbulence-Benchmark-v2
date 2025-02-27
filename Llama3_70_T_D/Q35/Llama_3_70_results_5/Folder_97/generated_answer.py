def remove_repeat_chars(s):
    char_count = {}
    char_to_remove = set()
    for char in s[34:69]:
        if char in char_count:
            char_count[char] += 1
            char_to_remove.add(char)
        else:
            char_count[char] = 1
    return ''.join([char for char in s if char not in char_to_remove])