def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    second_largest = None
    largest = None
    for num in nums[36:52]:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest:
            second_largest = num
    return second_largest