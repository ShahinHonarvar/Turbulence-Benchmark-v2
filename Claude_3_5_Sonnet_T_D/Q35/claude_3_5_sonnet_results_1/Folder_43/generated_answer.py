def remove_repeat_chars(string):
    if len(string) <= 29:
        return string
    substring = string[11:28]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result