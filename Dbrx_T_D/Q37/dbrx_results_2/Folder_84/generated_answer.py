def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 138 or i > 920 or (i >= 138 and i <= 920 and (ord(input_string[i]) < ord('6'))) or (i >= 138 and i <= 920 and (ord(input_string[i]) > ord('A'))):
            filtered_string += input_string[i]
    return filtered_string