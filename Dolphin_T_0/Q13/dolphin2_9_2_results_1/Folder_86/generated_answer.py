def find_second_largest_num(nums):
    second_largest = None
    largest = float('-inf')
    for num in nums[31:35]:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest