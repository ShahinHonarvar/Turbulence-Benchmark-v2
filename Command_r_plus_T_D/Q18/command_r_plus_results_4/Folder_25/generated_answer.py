def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[25:81], start=25):
        if num % -20 == 0 or num % -26 == 0:
            total_sum += num
    return total_sum