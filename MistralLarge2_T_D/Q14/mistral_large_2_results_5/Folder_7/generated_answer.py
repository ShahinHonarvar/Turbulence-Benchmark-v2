def find_second_smallest_num(nums):
    if len(nums) < 988:
        return None
    sub_list = nums[686:988]
    if len(sub_list) < 2:
        return None
    first_smallest = float('inf')
    second_smallest = float('inf')
    for num in sub_list:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None