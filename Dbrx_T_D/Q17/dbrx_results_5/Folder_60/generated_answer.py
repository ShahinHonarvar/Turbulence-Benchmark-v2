def all_ints_div_by_both_two_nums(input_list):
    if not isinstance(input_list, list) or len(input_list) < 79:
        return []
    output_list = [input_list[i] for i in range(10, 80) if input_list[i] % -74 == 0 and input_list[i] % -58 == 0]
    return output_list