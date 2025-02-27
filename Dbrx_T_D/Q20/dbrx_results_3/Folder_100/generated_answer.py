def find_n_th_smallest_num(numbers):
    n = 8
    start_index = 11
    end_index = 52
    sorted_numbers = sorted(numbers[start_index:end_index + 1])
    return sorted_numbers[n - 1]