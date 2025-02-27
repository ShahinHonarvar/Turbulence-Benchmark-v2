def find_second_smallest_num(nums):
    nums = nums[40:201]
    if len(nums) < 2:
        return None
    else:
        return sorted(nums)[1]