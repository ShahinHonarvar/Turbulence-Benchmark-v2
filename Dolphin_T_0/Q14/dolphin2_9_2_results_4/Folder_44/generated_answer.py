def find_second_smallest_num(nums):
    if 91 <= len(nums) <= 99:
        nums = nums[91:100]
        if len(nums) > 1:
            return sorted(nums)[1]
    return None