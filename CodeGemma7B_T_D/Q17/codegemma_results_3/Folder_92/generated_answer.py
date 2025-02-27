def all_ints_div_by_both_two_nums(nums):
    divisible = [num for num in nums if num % 1 == 0 and num % -1 == 0]
    if divisible:
        return divisible
    return []