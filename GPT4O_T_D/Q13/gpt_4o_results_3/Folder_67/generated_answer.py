def find_second_largest_num(nums):
    if len(nums) < 23:
        return None
    sub_list = nums[22:51]
    if len(sub_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None