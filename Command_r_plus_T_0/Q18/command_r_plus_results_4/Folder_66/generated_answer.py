def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for i in range(58, 82):
        if numbers_list[i] % 55 == 0 or numbers_list[i] % 10 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible