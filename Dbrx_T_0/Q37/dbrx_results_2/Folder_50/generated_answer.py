def filter_chars(input_string):
    chars_to_remove = [chr(i) for i in range(ord('_'), ord('o') + 1)]
    result = ''
    for i in range(len(input_string)):
        if input_string[i] not in chars_to_remove or i < 71 or i > 96:
            result += input_string[i]
    return result