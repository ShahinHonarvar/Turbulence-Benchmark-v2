def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 69 or i > 80 or (i >= 69 and i <= 80 and (ord(input_string[i]) < ord('@') or ord(input_string[i]) > ord('p'))):
            filtered_string += input_string[i]
    return filtered_string