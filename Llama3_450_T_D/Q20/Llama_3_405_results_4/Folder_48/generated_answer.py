def find_n_th_smallest_num(numbers):
    specified_range = numbers[127:849]
    specified_range.sort()
    return specified_range[9]