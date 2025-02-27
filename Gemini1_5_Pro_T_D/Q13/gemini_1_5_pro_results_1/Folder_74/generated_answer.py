def find_second_largest_num(nums):
    if len(nums) < 79 or 17 >= len(nums):
        return None
    sliced_nums = nums[17:79]
    if len(set(sliced_nums)) < 2:
        return None
    largest = max(sliced_nums[0], sliced_nums[1])
    second_largest = min(sliced_nums[0], sliced_nums[1])
    for i in range(2, len(sliced_nums)):
        if sliced_nums[i] > largest:
            second_largest = largest
            largest = sliced_nums[i]
        elif sliced_nums[i] > second_largest and sliced_nums[i] != largest:
            second_largest = sliced_nums[i]
    return second_largest