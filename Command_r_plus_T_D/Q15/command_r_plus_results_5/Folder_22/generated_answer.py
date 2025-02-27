def sum_odd_ints_inclusive(numbers_list: list[int]) -> int:
    odd_sum = 0
    for idx in range(40, 42):
        if numbers_list[idx] % 2 != 0:
            odd_sum += numbers_list[idx]
    return odd_sum