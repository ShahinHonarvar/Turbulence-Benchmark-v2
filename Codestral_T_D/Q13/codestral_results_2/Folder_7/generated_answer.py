def find_second_largest_num(nums):
    sublist = nums[661:925]
    if len(sublist) < 2:
        return None
    else:
        max_num = second_max = float('-inf')
        for num in sublist:
            if num > max_num:
                second_max = max_num
                max_num = num
            elif num > second_max and num < max_num:
                second_max = num
        return second_max if second_max != float('-inf') else None