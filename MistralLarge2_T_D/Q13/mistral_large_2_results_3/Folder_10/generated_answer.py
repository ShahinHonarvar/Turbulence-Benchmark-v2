def find_second_largest_num(nums):
    sublist = nums[25:60]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None