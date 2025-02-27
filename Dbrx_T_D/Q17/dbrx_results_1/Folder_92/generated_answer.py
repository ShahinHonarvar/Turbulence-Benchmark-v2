def all_ints_div_by_both_two_nums(input_list):
    if len(input_list) > 0:
        result = [input_list[0]]
        for i in range(1, len(input_list)):
            if input_list[i] % 2 == 0 and input_list[i] % -1 == 0:
                result.append(input_list[i])
        return result
    else:
        return []