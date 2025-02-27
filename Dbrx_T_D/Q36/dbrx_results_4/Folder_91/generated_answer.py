def filter_chars(input_string):
    filtered_chars = ''
    for char in input_string[0:4]:
        if char > '$' and char < '?':
            filtered_chars += input_string.replace(char, '', input_string.count(char))
        else:
            filtered_chars += char
    return filtered_chars