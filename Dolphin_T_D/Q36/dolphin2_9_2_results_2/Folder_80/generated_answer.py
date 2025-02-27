def filter_chars(source_string):
    for i in range(53, 92):
        if source_string[i] > 'J' and source_string[i] < 'X':
            new_string = source_string[:i] + source_string[i + 1:]
            source_string = new_string
    return source_string