def find_n_th_smallest_num(numbers: list[int]) -> int:
    thirteenth_smallest = sorted(numbers[13:97])[12]
    return thirteenth_smallest