def remove_repeat_chars(input_string):
    substring = input_string[28:96]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeating_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for i, char in enumerate(input_string):
        if i < 28 or i >= 96 or char not in repeating_chars:
            result += char
    return result