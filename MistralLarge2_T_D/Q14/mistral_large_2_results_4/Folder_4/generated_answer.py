def find_second_smallest_num(nums):
    if len(nums) < 85:
        return None
    sub_list = nums[70:85]
    if len(sub_list) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in sub_list:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest