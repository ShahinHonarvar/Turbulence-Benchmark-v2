def find_second_largest_num(nums):
    second_largest = None
    largest = float('-inf')
    for num in nums[36:77]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest