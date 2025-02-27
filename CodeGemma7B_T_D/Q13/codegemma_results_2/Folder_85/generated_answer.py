def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) <= 8 or all((num == nums[0] for num in nums[6:9])):
        return None
    return nums[7]