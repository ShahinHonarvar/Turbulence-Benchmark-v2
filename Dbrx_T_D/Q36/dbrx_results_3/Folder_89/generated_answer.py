def filter_chars(input_string):
    start_index = 57
    end_index = 69
    min_char = '('
    max_char = 'W'
    char_set = set()
    for i in range(len(input_string)):
        if i >= start_index and i < end_index:
            char = input_string[i]
            if char > min_char and char < max_char:
                char_set.add(char)
    result = ''
    for char in input_string:
        if char not in char_set:
            result += char
    return result