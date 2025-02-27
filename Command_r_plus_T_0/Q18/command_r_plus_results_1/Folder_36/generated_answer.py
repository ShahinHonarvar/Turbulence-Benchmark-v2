def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index in range(299, 383):
        if numbers_list[index] % 858 == 0 or numbers_list[index] % 952 == 0:
            sum_divisible += numbers_list[index]
    return sum_divisible