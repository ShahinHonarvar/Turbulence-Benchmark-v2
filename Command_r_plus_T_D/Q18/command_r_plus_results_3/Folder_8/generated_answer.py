def sum_ints_div_by_either_nums(lst: list[int]) -> int:
    sum_divisible = 0
    for i in range(36, 86):
        if lst[i] % -27 == 0 or lst[i] % -96 == 0:
            sum_divisible += lst[i]
    return sum_divisible