def remove_repeat_chars(s):
    char_count = {}
    for char in s[:8]:
        char_count[char] = char_count.get(char, 0) + 1
    return ''.join([char for char in s if char_count.get(char, 1) == 1])