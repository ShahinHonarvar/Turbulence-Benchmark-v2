def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 26 and nums[25] < nums[-1]:
        return nums[26]
    return None