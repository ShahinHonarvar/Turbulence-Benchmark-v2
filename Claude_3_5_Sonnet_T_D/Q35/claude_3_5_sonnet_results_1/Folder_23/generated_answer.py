def remove_repeat_chars(input_string):
    repeated_chars = set()
    for char in input_string[21:36]:
        if input_string[21:36].count(char) > 1:
            repeated_chars.add(char)
    result = ''
    for char in input_string:
        if char not in repeated_chars:
            result += char
    return result