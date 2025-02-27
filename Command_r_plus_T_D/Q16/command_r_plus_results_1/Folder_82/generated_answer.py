def sum_even_ints_inclusive(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[29:30]):
        if num % 2 == 0:
            total_sum += num
    return total_sum