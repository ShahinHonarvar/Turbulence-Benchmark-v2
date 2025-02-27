def find_second_smallest_num(numbers):
    nums = sorted(numbers[75:86])
    if len(nums) >= 2:
        return nums[1]
    else:
        return None