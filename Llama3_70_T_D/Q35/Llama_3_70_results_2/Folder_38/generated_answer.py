def remove_repeat_chars(input_string):
    char_count = {}
    for char in input_string[36:85]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    return ''.join((char for char in input_string if char not in repeat_chars))