def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    subset = nums[:6]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest is not None else None