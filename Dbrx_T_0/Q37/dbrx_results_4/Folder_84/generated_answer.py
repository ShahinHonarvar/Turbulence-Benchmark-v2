def filter_chars(input_string):
    start_index = 138
    end_index = 920
    chars_to_remove = [chr(i) for i in range(ord('6'), ord('A') + 1)]
    for i in range(start_index, end_index + 1):
        if input_string[i] in chars_to_remove:
            input_string = input_string[:i] + input_string[i + 1:]
            end_index -= 1
            i -= 1
    return input_string