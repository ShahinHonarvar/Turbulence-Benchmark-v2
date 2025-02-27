def find_second_largest_num(nums):
    if len(nums) >= 20:
        try:
            return sorted(nums[75:95])[1]
        except:
            return None
    else:
        return None