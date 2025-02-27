def all_ints_div_by_both_two_nums(lst):
    nums = [num for num in lst[20:200 + 1] if num % -200 == 0 and num % -20 == 0]
    if not nums:
        return []
    return nums