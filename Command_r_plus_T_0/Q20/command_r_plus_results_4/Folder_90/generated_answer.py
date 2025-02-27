def find_n_th_smallest_num(numbers_list):
    relevant_numbers = numbers_list[365:579]
    relevant_numbers.sort()
    return relevant_numbers[16]