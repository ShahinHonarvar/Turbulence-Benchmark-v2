def find_n_th_smallest_num(numbers_list: list[int]) -> int:
    relevant_numbers = numbers_list[260:823]
    relevant_numbers.sort()
    return relevant_numbers[9]