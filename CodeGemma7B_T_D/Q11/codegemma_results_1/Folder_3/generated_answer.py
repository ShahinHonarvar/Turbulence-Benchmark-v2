def find_largest_num(nums):
    largest = None
    for num in nums[62:93]:
        if largest is None or num > largest:
            largest = num
    return largest