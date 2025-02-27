def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    nums.sort()
    return nums[1]