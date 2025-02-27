def find_n_th_smallest_num(numbers):
    relevant_numbers = numbers[12:91]
    relevant_numbers.sort()
    return relevant_numbers[16]