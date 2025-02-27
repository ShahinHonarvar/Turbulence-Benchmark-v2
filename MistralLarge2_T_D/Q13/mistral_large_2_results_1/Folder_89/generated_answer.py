def find_second_largest_num(nums):
    subset = nums[56:83]
    if len(subset) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in subset:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None