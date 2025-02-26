def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = max(nums[0:1])
    second_largest = None
    for num in nums[0:1]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest