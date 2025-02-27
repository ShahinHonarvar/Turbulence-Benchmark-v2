def return_nth_smallest_ascii(string):
    input_list = list(string[17:57])
    output_list = sorted(input_list, key=ord)
    return output_list[8]