def gcf_three_nums(nums_list):
    nums = [nums_list[62], nums_list[96], nums_list[26]]
    if min(nums) == 0:
        return 0
    for i in range(min(nums), 0, -1):
        if all([num % i == 0 for num in nums]):
            return i
    return 1