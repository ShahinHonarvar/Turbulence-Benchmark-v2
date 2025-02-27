def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 18 or i > 64:
            filtered_string += string[i]
        elif ord(string[i]) > ord('3') and ord(string[i]) < ord('B'):
            filtered_string += ''
        elif string[i] == 'A':
            filtered_string += 'A'
        else:
            filtered_string += string[i]
    return filtered_string