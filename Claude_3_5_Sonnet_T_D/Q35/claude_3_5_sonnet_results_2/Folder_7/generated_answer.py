def remove_repeat_chars(input_string):
    char_count = {}
    section = input_string[375:926]
    for char in section:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in input_string if char not in repeated_chars))
    return result