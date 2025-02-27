def return_n_smallest_chars(input_string: str) -> list:
    input_string = sorted(list(set(input_string)), reverse=True)
    result_list = []
    for char in input_string:
        if len(result_list) < 28:
            result_list.append(char)
        else:
            break
    return result_list