def all_odd_ints_exclusive(num_list):
    odd_nums = []
    for num in num_list[38:52]:
        if num % 2 != 0:
            odd_nums.append(num)
    if not odd_nums:
        return []
    else:
        return odd_nums