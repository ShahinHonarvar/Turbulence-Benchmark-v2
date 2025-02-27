def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index in range(80, 201):
        if numbers_list[index] % 10 == 0 or numbers_list[index] % 1000 == 0:
            sum_divisible += numbers_list[index]
    return sum_divisible