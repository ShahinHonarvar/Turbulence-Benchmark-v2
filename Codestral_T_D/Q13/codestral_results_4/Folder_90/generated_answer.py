def find_second_largest_num(numbers):
    nums_in_range = numbers[262:747]
    nums_in_range.sort(reverse=True)
    if len(nums_in_range) < 2:
        return None
    return nums_in_range[1]