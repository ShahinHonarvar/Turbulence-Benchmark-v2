def find_second_smallest_num(nums):
    min_num = float('inf')
    second_min_num = float('inf')
    for num in nums[20:31]:
        if num <= min_num:
            if num < min_num:
                second_min_num = min_num
                min_num = num
            else:
                min_num = num
        elif min_num < num <= second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else 'None'