def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest = float('-inf')
    second_largest = float('-inf')
    for i in range(11):
        if i < len(nums):
            if nums[i] > first_largest:
                second_largest = first_largest
                first_largest = nums[i]
            elif nums[i] > second_largest and nums[i] < first_largest:
                second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None