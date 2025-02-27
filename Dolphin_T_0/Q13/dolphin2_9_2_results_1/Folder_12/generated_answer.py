def find_second_largest_num(nums):
    if not all((isinstance(num, (float, int)) for num in nums[14:65])):
        return None
    nums = [num for num in nums[14:65] if isinstance(num, (float, int))]
    if len(nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest