def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_ = 0
    for index in range(28, 97):
        if numbers_list[index] % 90 == 0 or numbers_list[index] % 97 == 0:
            sum_ += numbers_list[index]
    return sum_