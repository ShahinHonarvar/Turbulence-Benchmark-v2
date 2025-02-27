def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 11:
        return None
    largest = max(nums[0:11])
    second_largest = min(nums[0:11])
    for i in range(len(nums)):
        if i > 10:
            break
        if nums[i] != largest and nums[i] > second_largest:
            second_largest = nums[i]
    if second_largest != largest:
        return second_largest
    else:
        return None