def find_second_largest_num(nums):
    nums.sort(reverse=True)
    for num in nums[40:201]:
        if len(nums) < 41:
            return None
        if len(nums) > 40:
            return nums[41]
        return num