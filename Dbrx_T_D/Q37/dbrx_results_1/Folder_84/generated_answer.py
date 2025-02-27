def filter_chars(input_string):
    filtered_string = ''
    for i in range(min(920, len(input_string)), max(138, 0), -1):
        if '6' <= input_string[i] <= 'A':
            filtered_string = filtered_string[:i] + filtered_string[i + 1:]
    return filtered_string