def find_n_th_smallest_num(numbers: list[int]) -> int:
    numbers_subset = numbers[10:101]
    numbers_subset.sort()
    return numbers_subset[9]