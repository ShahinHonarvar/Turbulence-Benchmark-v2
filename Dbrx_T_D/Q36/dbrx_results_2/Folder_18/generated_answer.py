def filter_chars(input_str):
    start_index = 587
    end_index = 648
    filtered_chars = []
    for i in range(len(input_str)):
        if i >= start_index and i < end_index:
            char = input_str[i]
            if char > ',' and char < 'c':
                continue
        filtered_chars.append(input_str[i])
    return ''.join(filtered_chars)