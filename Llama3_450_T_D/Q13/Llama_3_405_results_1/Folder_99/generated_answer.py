def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in nums[310:371]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    if second_largest != float('-inf'):
        return second_largest
    return None