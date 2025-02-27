def find_second_largest_num(nums):
    if len(nums) < 81:
        return None
    largest = second_largest = float('-inf')
    for num in nums[40:81]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None