def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for char in s[10:80]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])