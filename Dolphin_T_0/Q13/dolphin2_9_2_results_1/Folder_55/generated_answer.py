def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] < largest:
            second_largest = nums[i]
    if second_largest != float('-inf'):
        return second_largest
    else:
        return None