def filter_chars(input_string):
    start_index = 27
    end_index = 85
    ascii_start = ord('!')
    ascii_end = ord('B')
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= start_index and i <= end_index and (ord(input_string[i]) >= ascii_start) and (ord(input_string[i]) <= ascii_end):
            continue
        filtered_string += input_string[i]
    return filtered_string