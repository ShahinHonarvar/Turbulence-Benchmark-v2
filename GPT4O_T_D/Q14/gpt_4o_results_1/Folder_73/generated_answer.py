def find_second_smallest_num(nums):
    if len(nums) < 98 or len(nums[59:98]) < 2:
        return None
    sub_list = nums[59:98]
    first_min = float('inf')
    second_min = float('inf')
    for num in sub_list:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None