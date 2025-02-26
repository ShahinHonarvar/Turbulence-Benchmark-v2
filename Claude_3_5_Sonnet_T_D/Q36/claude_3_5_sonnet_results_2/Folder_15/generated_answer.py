def filter_chars(input_string):
    filtered_chars = set()
    for char in input_string[3:7]:
        if 'h' < char < 'k':
            filtered_chars.add(char)
    result = ''.join((char for char in input_string if char not in filtered_chars))
    return result