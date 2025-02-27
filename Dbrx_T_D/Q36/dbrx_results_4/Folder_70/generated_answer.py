def filter_chars(input_string: str) -> str:
    start_index = 170
    end_index = 195
    char_range = tuple((ord(c) for c in input_string[start_index:end_index]))
    char_set = {chr(i) for i in range(ord('!') + 1, ord('}') - 1) if i not in char_range}
    for char in char_set:
        input_string = input_string.replace(char, '')
    return input_string