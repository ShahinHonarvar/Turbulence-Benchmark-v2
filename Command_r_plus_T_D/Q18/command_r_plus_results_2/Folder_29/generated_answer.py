def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for idx in range(55, 85):
        if numbers_list[idx] % -24 == 0 or numbers_list[idx] % -11 == 0:
            sum_divisible_nums += numbers_list[idx]
    return sum_divisible_nums