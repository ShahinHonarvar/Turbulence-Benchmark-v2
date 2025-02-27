def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    total_sum = 0
    for i in range(10, 77):
        if lst[i] % -40 == 0 or lst[i] % -12 == 0:
            total_sum += lst[i]
    return total_sum