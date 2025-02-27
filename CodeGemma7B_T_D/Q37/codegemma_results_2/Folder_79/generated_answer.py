def filter_chars(string):
    filtered_string = ''.join([char for char in string if not (string[index] >= '@' and string[index] <= 'T' and (10 <= index <= 52)) for index in range(len(string))])
    return filtered_string