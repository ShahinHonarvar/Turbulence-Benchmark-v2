def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    total_sum = 0
    for idx in range(20, 201):
        if lst[idx] % -20 == 0 or lst[idx] % -200 == 0:
            total_sum += lst[idx]
    return total_sum