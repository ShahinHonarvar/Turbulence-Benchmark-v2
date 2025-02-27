def all_ints_div_by_num(int_list):
    output_list = []
    for num in int_list[70:72]:
        if num % 85 == 0:
            output_list.append(num)
    return output_list