def find_second_largest_num(nums):
    nums.sort(reverse=True)
    return nums[31:73][1] if len(nums[31:73]) > 1 else 'None'