def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    sum_odd = 0
    for index in range(40, 42):
        if numbers_list[index] % 2 != 0:
            sum_odd += numbers_list[index]
    return sum_odd