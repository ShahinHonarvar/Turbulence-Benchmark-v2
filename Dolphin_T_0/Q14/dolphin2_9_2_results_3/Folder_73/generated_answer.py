def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 59:
        return 'None'
    else:
        sub_nums = nums[59:98]
        sub_nums.sort()
        return sub_nums[1]