def sum_ints_div_by_either_nums(numbers: list[int]) -> int:
    total_sum = 0
    for idx in range(6):
        if numbers[idx] % -1 == 0 or numbers[idx] % 13 == 0:
            total_sum += numbers[idx]
    return total_sum