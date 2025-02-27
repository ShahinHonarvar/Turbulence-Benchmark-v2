def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 101:
        return nums[100:201][1]
    else:
        return 'None'