def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) <= 4:
        return None
    return nums[4:5]