def find_second_smallest_num(numbers):
    nums_310_370 = sorted(numbers[310:371])
    if len(nums_310_370) < 2:
        return None
    return nums_310_370[1]