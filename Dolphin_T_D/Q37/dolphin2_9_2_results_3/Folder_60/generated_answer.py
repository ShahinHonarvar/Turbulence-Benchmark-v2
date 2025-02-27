def filter_chars(input_str):
    result = ''
    chars_to_filter = set()
    for i in range(12, 78):
        char = input_str[i]
        if ord(':') <= ord(char) <= ord('L'):
            chars_to_filter.add(char)
    for char in input_str:
        if char not in chars_to_filter:
            result += char
    return result