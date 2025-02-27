def find_second_largest_num(numbers):
    if len(numbers) <= 8:
        return None
    nums = numbers[4:9]
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]