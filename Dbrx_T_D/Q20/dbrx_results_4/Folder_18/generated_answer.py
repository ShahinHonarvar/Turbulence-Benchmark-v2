def find_n_th_smallest_num(numbers):
    n = 6
    start_index = 42
    end_index = 67
    sorted_numbers = sorted(numbers)
    sublist = sorted_numbers[start_index:end_index + 1]
    return sublist[n - 1]