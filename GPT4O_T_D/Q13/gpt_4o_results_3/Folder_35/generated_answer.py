def find_second_largest_num(nums):
    if len(nums) < 49:
        return None
    sublist = nums[30:49]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None