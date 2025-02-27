def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 19 or i > 90:
            filtered_string += input_string[i]
            continue
        if ord(input_string[i]) >= ord('F') and ord(input_string[i]) <= ord('h'):
            continue
        if ord(input_string[i]) >= 90 and ord(input_string[i]) <= 102:
            continue
        filtered_string += input_string[i]
    return filtered_string