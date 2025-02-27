def find_second_smallest_num(numbers):
    if 76 < len(numbers):
        nums_slice = numbers[37:77]
        nums_sorted = sorted(nums_slice)
        if len(nums_sorted) > 1:
            return nums_sorted[1]
    return None