def remove_repeat_chars(input_string):
    if len(input_string) <= 35:
        return input_string
    start = 35
    end = min(69, len(input_string))
    substring = input_string[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for i, char in enumerate(input_string):
        if i < start or i >= end or char not in chars_to_remove:
            result += char
    return result