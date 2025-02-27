def find_second_smallest_num(nums):
    if len(nums) < 97:
        return None
    sublist = nums[59:98]
    try:
        return sorted(sublist)[1]
    except:
        return None