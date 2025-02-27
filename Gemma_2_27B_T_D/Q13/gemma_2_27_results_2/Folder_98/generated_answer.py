def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[:7])
    second_largest = min(nums[:7])
    for num in nums[:7]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None