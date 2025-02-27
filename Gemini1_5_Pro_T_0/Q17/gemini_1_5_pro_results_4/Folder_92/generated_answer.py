def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(0, 1):
        if i >= len(nums):
            break
        num = nums[i]
        if num % 1 == 0 and num % -1 == 0:
            result.append(num)
    return result