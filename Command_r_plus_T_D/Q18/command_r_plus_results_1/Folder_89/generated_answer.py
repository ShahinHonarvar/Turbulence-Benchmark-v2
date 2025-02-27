def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[28:97], start=28):
        if num % 90 == 0 or num % 97 == 0:
            total_sum += num
    return total_sum