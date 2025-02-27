def find_second_largest_num(numbers):
    nums_in_range = sorted(numbers[40:81], reverse=True)
    if len(nums_in_range) < 2:
        return None
    return nums_in_range[1]