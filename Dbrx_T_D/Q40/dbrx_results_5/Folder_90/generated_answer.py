def return_n_smallest_chars(input_string: str) -> list:
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort()
    result_list = [chr(char) for char in ascii_list[:24]]
    result_list.sort(reverse=True)
    return result_list