def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) - 10 >= 66 and nums[66] != max(nums):
        return nums[66]
    else:
        return None