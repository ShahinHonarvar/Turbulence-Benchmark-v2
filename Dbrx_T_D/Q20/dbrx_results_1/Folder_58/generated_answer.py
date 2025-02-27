def find_n_th_smallest_num(numbers):
    relevant_numbers = numbers[145:157]
    n_th_smallest = sorted(relevant_numbers)[5]
    return n_th_smallest