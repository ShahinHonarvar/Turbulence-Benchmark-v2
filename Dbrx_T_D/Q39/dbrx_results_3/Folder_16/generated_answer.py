def return_n_greatest_chars(input_string):
    input_list = list(input_string.encode())
    input_list.sort(reverse=True)
    return [chr(i) for i in input_list][:64]