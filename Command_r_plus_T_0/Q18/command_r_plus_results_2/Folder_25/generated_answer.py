def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[25:81], start=25):
        if number % -20 == 0 or number % -26 == 0:
            total_sum += number
    return total_sum