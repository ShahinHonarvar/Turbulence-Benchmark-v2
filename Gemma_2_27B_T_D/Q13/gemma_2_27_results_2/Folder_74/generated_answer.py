def find_second_largest_num(nums):
    try:
        return sorted(nums[17:79])[-2]
    except:
        return None