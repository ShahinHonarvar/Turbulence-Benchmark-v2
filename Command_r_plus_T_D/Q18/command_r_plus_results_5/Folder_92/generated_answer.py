def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for number in numbers_list:
        if number % 1 == 0 or number % -1 == 0:
            total_sum += number
    return total_sum