def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 7:
        return None
    return nums[1]