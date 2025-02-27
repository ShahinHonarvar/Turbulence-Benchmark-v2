def find_second_largest_num(nums):
    if not nums:
        return None
    largest = nums[59]
    second_largest = None
    for num in nums[60:98]:
        if largest < num:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest