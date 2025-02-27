def find_second_largest_num(nums):
    second_largest = None
    largest = float('-inf')
    for num in nums[74:96]:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest