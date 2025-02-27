def remove_repeat_chars(s):
    if len(s) <= 355:
        return s
    start_index = 356
    end_index = min(988, len(s) - 1)
    char_count = {}
    for char in s[start_index:end_index]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result