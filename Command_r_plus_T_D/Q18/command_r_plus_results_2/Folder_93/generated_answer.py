def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for idx in range(86, 90):
        if numbers_list[idx] % -61 == 0 or numbers_list[idx] % -79 == 0:
            sum_divisible += numbers_list[idx]
    return sum_divisible