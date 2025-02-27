def sum_even_ints_inclusive(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(8, 81):
        if numbers_list[index] % 2 == 0:
            total_sum += numbers_list[index]
    return total_sum