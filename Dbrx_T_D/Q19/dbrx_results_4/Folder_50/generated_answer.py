def all_ints_not_div_by_num(num_list):
    range_indices = slice(13, 76, 44)
    divisible_by_44 = set(range(44, max(num_list), 44))
    return [num for num in num_list[range_indices] if num not in divisible_by_44]