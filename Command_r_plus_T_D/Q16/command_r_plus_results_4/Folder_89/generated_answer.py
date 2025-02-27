def sum_even_ints_inclusive(numbers_list: list[int]) -> int:
    sum_even_integers = 0
    for index in range(56, 83):
        if numbers_list[index] % 2 == 0:
            sum_even_integers += numbers_list[index]
    return sum_even_integers