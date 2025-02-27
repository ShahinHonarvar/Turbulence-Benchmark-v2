def find_second_largest_num(nums):
    try:
        return sorted(nums[19:93])[-2]
    except:
        return None