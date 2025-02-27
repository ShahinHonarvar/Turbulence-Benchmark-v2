def find_n_th_smallest_num(numbers):
    start_index = 25
    end_index = 64
    n = 12
    relevant_elements = numbers[start_index:end_index + 1]
    relevant_elements.sort()
    return relevant_elements[n - 1]