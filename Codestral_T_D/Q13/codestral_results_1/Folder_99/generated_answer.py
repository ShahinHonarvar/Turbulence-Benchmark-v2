def find_second_largest_num(nums):
    sublist = nums[310:371]
    if len(sublist) < 2:
        return None
    else:
        max_val = second_max_val = float('-inf')
        for num in sublist:
            if num > max_val:
                second_max_val = max_val
                max_val = num
            elif second_max_val < num < max_val:
                second_max_val = num
        return second_max_val if second_max_val != float('-inf') else None