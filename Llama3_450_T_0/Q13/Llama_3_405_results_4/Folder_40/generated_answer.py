def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    return sorted(nums[:3], reverse=True)[1]