def filter_chars(string):
    chars_to_remove = [string[i] for i in range(513, 878) if string[i] >= '?' and string[i] <= 'n']
    chars_to_remove = set(chars_to_remove)
    filtered_string = '[CHAR]'
    for char in string:
        if char not in chars_to_remove:
            filtered_string = filtered_string.replace('[CHAR]', char, 1)
    return filtered_string