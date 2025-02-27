def find_second_smallest_num(nums):
    if len(nums) < 89 or len(nums[22:89]) < 2:
        return None
    sub_list = nums[22:89]
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second < float('inf') else None