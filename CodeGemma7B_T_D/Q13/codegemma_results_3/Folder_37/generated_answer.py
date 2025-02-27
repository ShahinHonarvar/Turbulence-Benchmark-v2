def find_second_largest_num(nums):
    if len(nums) <= 5 or not nums or (not all((isinstance(num, int) for num in nums))):
        return None
    nums.sort(reverse=True)
    for i in range(1, 6):
        if i < len(nums):
            return nums[i]
    return None