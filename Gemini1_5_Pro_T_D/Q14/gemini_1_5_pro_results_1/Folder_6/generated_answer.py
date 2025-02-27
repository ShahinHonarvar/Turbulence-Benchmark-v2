def find_second_smallest_num(nums):
    if len(nums) < 80:
        return None
    else:
        sub_nums = nums[29:80]
        sub_nums.sort()
        return sub_nums[1]