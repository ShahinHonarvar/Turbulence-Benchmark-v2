def filter_chars(input_str):
    chars_to_remove = set()
    for i in range(42, 98):
        if input_str[i] >= '*' and input_str[i] <= 'b':
            chars_to_remove.add(input_str[i])
    result = []
    for char in input_str:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)