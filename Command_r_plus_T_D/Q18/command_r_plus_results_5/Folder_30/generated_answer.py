def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    total_sum = 0
    for idx in range(11, 77):
        if lst[idx] % -81 == 0 or lst[idx] % -94 == 0:
            total_sum += lst[idx]
    return total_sum