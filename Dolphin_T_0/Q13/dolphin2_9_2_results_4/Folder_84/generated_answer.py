def find_second_largest_num(input_list):
    sublist = input_list[42:87]
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    else:
        sorted_nums = sorted(unique_nums)
        return sorted_nums[-2]