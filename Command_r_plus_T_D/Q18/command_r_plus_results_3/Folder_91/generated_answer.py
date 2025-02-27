def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_numbers = 0
    for idx in range(5):
        if numbers_list[idx] % 8 == 0 or numbers_list[idx] % -3 == 0:
            sum_divisible_numbers += numbers_list[idx]
    return sum_divisible_numbers