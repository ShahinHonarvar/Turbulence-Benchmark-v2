def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    sum_odd = 0
    for i in range(64, 67):
        if numbers_list[i] % 2 != 0:
            sum_odd += numbers_list[i]
    return sum_odd