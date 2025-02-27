def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    total_sum = 0
    for i in range(6, len(numbers_list)):
        if numbers_list[i] % 2 != 0:
            total_sum += numbers_list[i]
    return total_sum