def find_second_largest_num(nums):
    if not nums:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in nums[62:64]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest