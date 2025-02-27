def return_n_greatest_chars(input_str):
    input_str = ''.join(set(input_str))
    input_str = input_str[-84:]
    input_str = sorted(input_str, key=ord, reverse=True)
    return input_str