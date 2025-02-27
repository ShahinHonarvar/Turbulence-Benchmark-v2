def find_second_largest_num(nums):
    if not nums or len(nums) < 3:
        return 'None'
    largest = float('-inf')
    second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest < float('-inf') or second_largest == largest:
        return 'None'
    return second_largest