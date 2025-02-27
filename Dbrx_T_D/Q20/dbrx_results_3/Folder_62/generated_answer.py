def find_n_th_smallest_num(numbers):
    if len(numbers) < 72:
        return 'Input list should have at least 72 numbers'
    sub_list = numbers[51:72]
    sorted_sub_list = sorted(set(sub_list))
    if 9 > len(sorted_sub_list):
        return 'There are less than 9 distinct numbers in the specified range of the input list'
    return sorted_sub_list[8]