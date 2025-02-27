def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for i in range(7, len(numbers_list)):
        if numbers_list[i] % 5 == 0 or numbers_list[i] % 7 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible