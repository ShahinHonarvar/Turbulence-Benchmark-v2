def find_n_th_smallest_num(numbers):
    specified_range = numbers[299:636]
    specified_range.sort()
    return specified_range[11]