def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 52 or min(nums) < -2147483648 or (max(nums) > 2147483647):
        return None
    second_largest = None
    largest = None
    for num in nums[29:52]:
        if largest is None or num > largest:
            largest = num
            second_largest = None
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest