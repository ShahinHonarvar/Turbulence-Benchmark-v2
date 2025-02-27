def find_n_th_smallest_num(numbers: list[int]) -> int:
    fifth_smallest = sorted(numbers[5:10])[4]
    return fifth_smallest