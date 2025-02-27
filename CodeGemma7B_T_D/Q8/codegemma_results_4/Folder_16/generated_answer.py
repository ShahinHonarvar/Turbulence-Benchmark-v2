def all_even_ints_exclusive(num_list):
    if not num_list:
        return []
    nums = [num for num in num_list[86:90] if num % 2 == 0 and num != 0]
    if not nums:
        return []
    return nums