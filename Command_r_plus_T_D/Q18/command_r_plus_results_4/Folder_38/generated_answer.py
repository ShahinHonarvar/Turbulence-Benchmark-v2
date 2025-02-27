def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for i in range(10, 77):
        if numbers_list[i] % -40 == 0 or numbers_list[i] % -12 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible