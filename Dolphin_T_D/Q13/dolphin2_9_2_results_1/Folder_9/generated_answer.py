def find_second_largest_num(nums):
    if 200 < len(nums) <= 201:
        return 'None'
    else:
        nums = nums[200:202]
        nums.sort()
        return nums[-2]