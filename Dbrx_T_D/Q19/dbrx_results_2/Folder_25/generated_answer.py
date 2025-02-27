def all_ints_not_div_by_num(input_list):
    low, high = (29, 53)
    result = [num for num in input_list[low:high] if num % -68 != 0]
    return result