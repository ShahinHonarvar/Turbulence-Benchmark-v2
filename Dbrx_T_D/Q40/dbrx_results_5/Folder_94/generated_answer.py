def return_n_smallest_chars(input_str: str) -> str:
    n = 87
    if n < 1:
        raise ValueError('n must be greater than zero')
    input_str_list = sorted(input_str, key=ord)
    return input_str_list[::-1][:n]