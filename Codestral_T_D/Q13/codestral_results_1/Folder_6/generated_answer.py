def find_second_largest_num(nums):
    sliced_nums = nums[10:67]
    sliced_nums.sort(reverse=True)
    return None if len(sliced_nums) < 2 else sliced_nums[1]