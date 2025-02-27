def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_ = 0
    for i in range(38, 53):
        if numbers_list[i] % -41 == 0 or numbers_list[i] % -47 == 0:
            sum_ += numbers_list[i]
    return sum_