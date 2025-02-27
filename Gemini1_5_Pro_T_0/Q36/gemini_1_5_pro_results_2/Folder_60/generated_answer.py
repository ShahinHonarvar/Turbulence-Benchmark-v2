def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(23, 83):
        if i < len(input_string) and 'f' < input_string[i] < 'o':
            chars_to_remove.add(input_string[i])
    result = []
    for char in input_string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)