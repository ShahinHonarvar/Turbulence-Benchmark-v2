def find_second_smallest_num(nums):
    nums = sorted(nums[70:85])
    if len(nums) <= 1:
        return None
    return nums[1]