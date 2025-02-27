def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_numbers = 0
    for index in range(93, 95):
        if numbers_list[index] % -53 == 0 or numbers_list[index] % -91 == 0:
            sum_divisible_numbers += numbers_list[index]
    return sum_divisible_numbers