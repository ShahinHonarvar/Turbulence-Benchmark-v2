def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[13:77], start=13):
        if number % -66 == 0 or number % -32 == 0:
            total_sum += number
    return total_sum