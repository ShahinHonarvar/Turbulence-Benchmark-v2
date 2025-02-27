def sum_even_ints_inclusive(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list):
        if 111 <= index <= 111 and number % 2 == 0:
            total_sum += number
    return total_sum