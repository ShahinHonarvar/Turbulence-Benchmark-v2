def find_second_smallest_num(nums):
    sub_list = nums[55:99]
    if len(sub_list) < 2:
        return None
    smallest = min(sub_list)
    second_smallest = float('inf')
    for num in sub_list:
        if num < second_smallest and num > smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None