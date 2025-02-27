def find_second_smallest_num(nums):
    if len(nums) >= 2 and len(set(nums[:4])) == 4:
        return sorted(nums[:4])[1]
    return None