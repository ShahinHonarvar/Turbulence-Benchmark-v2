def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    total_sum = 0
    for i in range(200, len(lst)):
        if lst[i] % 17 == 0 or lst[i] % -5 == 0:
            total_sum += lst[i]
    return total_sum