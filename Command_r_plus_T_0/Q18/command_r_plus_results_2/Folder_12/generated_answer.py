def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for i in range(35, 65):
        if numbers_list[i] % -30 == 0 or numbers_list[i] % -95 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible