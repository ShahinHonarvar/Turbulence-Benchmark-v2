def find_second_largest_num(nums):
    if len(nums[:10]) < 2:
        return None
    return sorted(nums[:10], reverse=True)[1]