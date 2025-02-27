def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[:9])
    second_largest = min(nums[:9])
    for num in nums[:9]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None