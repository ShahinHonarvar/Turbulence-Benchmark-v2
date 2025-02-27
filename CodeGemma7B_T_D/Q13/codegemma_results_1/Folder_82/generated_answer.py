def find_second_largest_num(nums):
    if 20 <= len(nums) <= 200:
        nums.sort(reverse=True)
        return nums[20]
    else:
        return 'None'