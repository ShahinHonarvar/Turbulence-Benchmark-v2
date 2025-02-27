def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 35 <= i <= 51 and 'H' <= string[i] <= 's':
            if string[i] not in filtered_string:
                filtered_string += string[i]
        else:
            filtered_string += string[i]
    return filtered_string