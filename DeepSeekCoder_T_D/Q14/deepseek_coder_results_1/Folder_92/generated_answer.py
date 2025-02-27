def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    first_min = min(nums[:2])
    second_min = max(nums[:2])
    return second_min if second_min != first_min else None