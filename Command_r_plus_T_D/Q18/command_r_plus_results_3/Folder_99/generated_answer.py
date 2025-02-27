def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    total_sum = 0
    for i in range(154, 799):
        if lst[i] % 275 == 0 or lst[i] % 580 == 0:
            total_sum += lst[i]
    return total_sum