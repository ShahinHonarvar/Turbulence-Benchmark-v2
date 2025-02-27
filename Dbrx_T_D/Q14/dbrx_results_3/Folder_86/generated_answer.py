def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    min_nums = sorted(numbers[33:37])
    if min_nums[0] != min_nums[1] and min_nums[1] != min_nums[2]:
        return min_nums[1]
    else:
        return None