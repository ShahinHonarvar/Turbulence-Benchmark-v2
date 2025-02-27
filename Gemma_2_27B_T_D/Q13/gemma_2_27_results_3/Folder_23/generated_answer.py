def find_second_largest_num(nums):
    try:
        return sorted(nums[52:72])[-2]
    except:
        return None