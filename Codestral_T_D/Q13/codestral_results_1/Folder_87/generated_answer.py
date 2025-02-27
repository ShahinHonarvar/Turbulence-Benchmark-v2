def find_second_largest_num(nums):
    sublist = nums[36:47]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest