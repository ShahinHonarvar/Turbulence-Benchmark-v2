def find_second_smallest_num(numbers):
    nums = sorted(numbers[33:37])
    if len(nums) > 1:
        return nums[1]
    else:
        return None