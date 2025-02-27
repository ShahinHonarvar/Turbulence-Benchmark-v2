def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[32:100], 32):
        if num % -11 == 0 or num % -15 == 0:
            total_sum += num
    return total_sum