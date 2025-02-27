def filter_chars(input_string):
    start_index = 344
    end_index = 874
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= start_index and i < end_index:
            char = input_string[i]
            if char > 'f' and char < '~':
                input_string = input_string[:i] + input_string[i + 1:]
                i -= 1
            else:
                filtered_string += char
    return filtered_string + input_string[end_index:]