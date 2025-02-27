def remove_repeat_chars(s):
    chars_to_remove = set()
    char_count = {}
    for i in range(409, 502):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
            if char_count[char] > 1:
                chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])