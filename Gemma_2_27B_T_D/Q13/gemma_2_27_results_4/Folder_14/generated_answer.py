def find_second_largest_num(nums):
    try:
        return sorted(nums[5:8])[-2]
    except:
        return None