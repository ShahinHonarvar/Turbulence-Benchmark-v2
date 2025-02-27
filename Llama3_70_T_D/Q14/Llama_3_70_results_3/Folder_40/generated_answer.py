def find_second_smallest_num(numbers):
    nums = sorted(numbers[:3])
    return nums[1] if len(nums) > 1 else None