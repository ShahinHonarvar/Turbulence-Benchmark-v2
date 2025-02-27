def find_second_smallest_num(nums):
    if len(nums) < 33:
        return None
    else:
        l = nums[28:33]
        l.sort()
        return l[1]