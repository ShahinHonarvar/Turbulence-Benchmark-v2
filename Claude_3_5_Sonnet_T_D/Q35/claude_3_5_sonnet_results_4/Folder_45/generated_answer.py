def remove_repeat_chars(input_string):
    if len(input_string) <= 201:
        return input_string
    start, end = (41, 200)
    substring = input_string[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result