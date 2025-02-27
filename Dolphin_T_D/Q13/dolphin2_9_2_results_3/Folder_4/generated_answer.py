def find_second_largest_num(nums):
    nums = nums[12:93]
    nums = [num for num in nums if nums.count(num) == 1]
    nums.sort()
    if len(nums) < 2:
        return None
    else:
        return nums[-2]