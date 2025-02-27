def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index in range(281, 695):
        if numbers_list[index] % -722 == 0 or numbers_list[index] % -731 == 0:
            sum_divisible += numbers_list[index]
    return sum_divisible