def find_second_largest_num(nums):
    if len(nums) < 80:
        return None
    sub_nums = nums[40:81]
    if len(set(sub_nums)) == 1:
        return None
    sub_nums.sort()
    return sub_nums[-2]