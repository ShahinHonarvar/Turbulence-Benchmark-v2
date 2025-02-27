def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    sliced_numbers = numbers_list[36:94]
    sliced_numbers.sort()
    return sliced_numbers[3]