def sum_even_ints_inclusive(numbers_list: list[int]) -> int:
    total = 0
    for index in range(661, 925):
        if numbers_list[index] % 2 == 0:
            total += numbers_list[index]
    return total