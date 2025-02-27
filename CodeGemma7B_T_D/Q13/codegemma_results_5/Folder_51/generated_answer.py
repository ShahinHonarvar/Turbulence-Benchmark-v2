def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 8 or not nums[1:9]:
        return None
    return nums[8]