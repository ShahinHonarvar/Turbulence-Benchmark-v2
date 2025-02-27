def find_second_largest_num(nums):
    try:
        return sorted(nums[64:67])[-2]
    except:
        return None