def find_second_largest_num(nums):
    nums_subset = nums[209:557]
    max_num = float('-inf')
    second_max = float('-inf')
    for num in nums_subset:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None