def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    sub_list = nums[27:56]
    if len(sub_list) < 2:
        return None
    first_smallest = second_smallest = float('inf')
    for num in sub_list:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None