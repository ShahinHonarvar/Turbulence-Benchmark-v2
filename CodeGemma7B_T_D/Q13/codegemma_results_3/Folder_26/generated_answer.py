def find_second_largest_num(nums):
    if len(nums) < 2 or nums[62] >= nums[99]:
        return None
    second_largest = nums[62]
    largest = nums[63]
    for i in range(64, 100):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    return second_largest