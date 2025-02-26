def filter_chars(input_string):
    result = ''
    chars_to_remove = set()
    for i in range(33, 61):
        if i < len(input_string) and '3' < input_string[i] < 'D':
            chars_to_remove.add(input_string[i])
    for char in input_string:
        if char not in chars_to_remove:
            result += char
    return result