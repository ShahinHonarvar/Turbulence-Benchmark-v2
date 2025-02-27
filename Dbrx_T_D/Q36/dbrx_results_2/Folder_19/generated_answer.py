def filter_chars(input_string):
    start_index = 77
    end_index = 87
    min_char = ';'
    max_char = 'r'

    def is_between(character, min_char, max_char):
        ascii_val = ord(character)
        min_ascii = ord(min_char)
        max_ascii = ord(max_char)
        return min_ascii < ascii_val < max_ascii
    characters_to_remove = [char for char in input_string[start_index:end_index] if is_between(char, min_char, max_char)]
    for char in characters_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string