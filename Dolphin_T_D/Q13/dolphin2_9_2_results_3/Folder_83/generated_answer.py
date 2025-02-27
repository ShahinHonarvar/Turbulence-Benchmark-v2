def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    elif len(nums) == 2:
        return min(nums) if max(nums) == nums[90] else max(nums)
    sublist = nums[90:91]
    max_num = sublist[0]
    second_max_num = float('-inf')
    for num in sublist:
        if num > max_num:
            max_num, second_max_num = (num, max_num)
        elif num < max_num and num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None