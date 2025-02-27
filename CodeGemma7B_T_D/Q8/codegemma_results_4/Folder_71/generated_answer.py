def all_even_ints_exclusive(number_list):
    output_list = []
    for number in number_list[36:54]:
        if number % 2 == 0:
            continue
        output_list.append(number)
    return output_list