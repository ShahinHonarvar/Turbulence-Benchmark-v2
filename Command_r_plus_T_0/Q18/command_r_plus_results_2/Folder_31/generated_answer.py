def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[56:89], start=56):
        if number % -59 == 0 or number % -79 == 0:
            total_sum += number
    return total_sum