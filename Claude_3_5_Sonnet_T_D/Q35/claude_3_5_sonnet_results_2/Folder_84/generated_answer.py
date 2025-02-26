def remove_repeat_chars(input_string):
    result = list(input_string)
    char_count = {}
    for i in range(33, 44):
        if i < len(input_string):
            char = input_string[i]
            char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in result if char not in chars_to_remove))