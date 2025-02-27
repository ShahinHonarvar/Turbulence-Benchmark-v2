def find_second_smallest_num(nums):
    subs = nums[80:200]
    if len(subs) < 2:
        return None
    subs.sort()
    return subs[1]