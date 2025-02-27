def find_second_largest_num(numbers):
    nums = sorted(numbers[:7], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]