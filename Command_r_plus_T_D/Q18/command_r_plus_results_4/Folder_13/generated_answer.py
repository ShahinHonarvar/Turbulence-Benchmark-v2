def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for i in range(13, 19):
        if numbers_list[i] % 45 == 0 or numbers_list[i] % 20 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible