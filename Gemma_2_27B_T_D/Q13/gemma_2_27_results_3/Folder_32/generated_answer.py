def find_second_largest_num(nums):
    try:
        return sorted(nums[21:98])[-2]
    except:
        return None