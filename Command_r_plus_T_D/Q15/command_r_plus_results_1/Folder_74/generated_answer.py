def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[17:79], 17):
        if number % 2 != 0:
            total_sum += number
    return total_sum