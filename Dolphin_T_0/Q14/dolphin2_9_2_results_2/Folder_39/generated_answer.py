def find_second_smallest_num(nums):
    if 28 <= 40 < len(nums):
        subnums = nums[28:41]
        subnums.sort()
        if len(subnums) > 1:
            return subnums[1]
    return None