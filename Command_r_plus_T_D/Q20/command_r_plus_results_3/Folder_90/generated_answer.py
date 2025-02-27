def find_n_th_smallest_num(numbers_list):
    start_index = 365
    end_index = 578
    relevant_numbers = numbers_list[start_index:end_index + 1]
    relevant_numbers.sort()
    return relevant_numbers[16]