def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index in range(41, 57):
        if numbers_list[index] % 82 == 0 or numbers_list[index] % 90 == 0:
            sum_divisible += numbers_list[index]
    return sum_divisible