def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 100:
        return nums[40:201][1]
    else:
        return 'None'