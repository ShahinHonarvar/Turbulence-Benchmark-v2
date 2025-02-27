def sum_ints_div_by_either_nums(numbers: list[int]) -> int:
    total_sum = 0
    for i in range(7):
        if numbers[i] % -5 == 0 or numbers[i] % -6 == 0:
            total_sum += numbers[i]
    return total_sum