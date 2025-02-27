def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    else:
        return sorted(nums[:5])[1] if len(set(nums[:5])) > 1 else None