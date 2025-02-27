def all_even_ints_inclusive(input_list):
    output_list = []
    for i in range(10, 101):
        if i % 2 == 0:
            output_list.append(i)
    return output_list