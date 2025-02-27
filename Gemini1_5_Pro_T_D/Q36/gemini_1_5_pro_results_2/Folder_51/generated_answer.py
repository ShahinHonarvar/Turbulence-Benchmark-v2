def filter_chars(text):
    filtered_string = ''
    for i in range(len(text)):
        char = text[i]
        if 58 <= i <= 81 and '5' < char < '>':
            continue
        filtered_string += char
    return filtered_string