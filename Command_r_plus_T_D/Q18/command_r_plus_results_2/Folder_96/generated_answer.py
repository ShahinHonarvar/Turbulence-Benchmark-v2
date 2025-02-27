def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[50:201], 50):
        if num % -34 == 0 or num % 64 == 0:
            total_sum += num
    return total_sum