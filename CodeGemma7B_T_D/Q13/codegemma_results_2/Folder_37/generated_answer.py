def find_second_largest_num(nums):
    if not nums or len(nums) < 7:
        return None
    nums.sort(reverse=True)
    return nums[6]