def find_second_smallest_num(nums):
    sub_nums = nums[64:67]
    if len(sub_nums) < 2:
        return None
    else:
        return sorted(sub_nums)[1]