def filter_chars(input_string):
    start_index = 22
    end_index = 85
    remove_chars = [char for char in range(ord('7'), ord('e') + 1) if char >= ord('7') and char <= ord('e')]
    result_string = ''
    for index, char in enumerate(input_string):
        if index < start_index or index > end_index or ord(char) not in remove_chars:
            result_string += char
    return result_string