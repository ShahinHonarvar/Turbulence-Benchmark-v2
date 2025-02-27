def find_second_largest_num(nums):
    if len(nums) <= 50 or len(nums) > 54:
        return 'None'
    nums.sort(reverse=True)
    return nums[50:55][1] if nums[50:55][1] != nums[0] else 'None'