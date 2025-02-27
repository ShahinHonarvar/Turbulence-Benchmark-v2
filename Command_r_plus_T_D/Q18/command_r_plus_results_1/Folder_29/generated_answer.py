def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_numbers = 0
    for i in range(55, 85):
        if numbers_list[i] % -24 == 0 or numbers_list[i] % -11 == 0:
            sum_divisible_numbers += numbers_list[i]
    return sum_divisible_numbers