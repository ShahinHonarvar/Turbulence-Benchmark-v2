def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index in range(40, 201):
        if numbers_list[index] % 21 == 0 or numbers_list[index] % 71 == 0:
            sum_divisible_nums += numbers_list[index]
    return sum_divisible_nums