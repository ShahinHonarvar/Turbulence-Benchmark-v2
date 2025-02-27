def find_second_largest_num(nums):
    if len(nums) < 101:
        return None
    largest = max(nums[100:201])
    second_largest = min(nums[100:201])
    for num in nums[100:201]:
        if num != largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None