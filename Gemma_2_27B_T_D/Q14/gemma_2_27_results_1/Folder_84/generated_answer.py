def find_second_smallest_num(nums):
    sub_nums = nums[40:81]
    if len(sub_nums) < 2:
        return None
    return sorted(set(sub_nums))[1]