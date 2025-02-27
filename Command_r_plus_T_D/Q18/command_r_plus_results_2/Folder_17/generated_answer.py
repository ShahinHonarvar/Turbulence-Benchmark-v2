def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_ = 0
    for index in range(81, 90):
        if numbers_list[index] % 56 == 0 or numbers_list[index] % 68 == 0:
            sum_ += numbers_list[index]
    return sum_