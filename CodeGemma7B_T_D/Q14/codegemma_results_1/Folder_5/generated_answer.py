def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    nums.sort()
    return nums[3:6]