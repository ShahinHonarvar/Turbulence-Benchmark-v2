def all_odd_ints_exclusive(int_list):
    odd_nums = []
    for num in range(52, 77):
        if num % 2 != 0:
            odd_nums.append(num)
    if not odd_nums:
        return []
    return odd_nums