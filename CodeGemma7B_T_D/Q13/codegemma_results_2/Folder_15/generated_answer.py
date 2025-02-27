def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest = None
    second_largest = None
    for num in nums:
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    if second_largest is None:
        return None
    return second_largest