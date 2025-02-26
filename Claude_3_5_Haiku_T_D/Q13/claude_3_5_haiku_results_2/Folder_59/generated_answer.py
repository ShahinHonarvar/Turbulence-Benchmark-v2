def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 10:
        return None
    first_ten = nums[:10]
    sorted_ten = sorted(set(first_ten), reverse=True)
    return sorted_ten[1] if len(sorted_ten) > 1 else None