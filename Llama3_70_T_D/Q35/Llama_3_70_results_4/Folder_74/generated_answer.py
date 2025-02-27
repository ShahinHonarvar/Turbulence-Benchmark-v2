def remove_repeat_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_to_remove = set()
    for char, count in char_count.items():
        if count > 1 and 69 < ord(char) < 97:
            char_to_remove.add(char)
    return ''.join([char for char in s if char not in char_to_remove])