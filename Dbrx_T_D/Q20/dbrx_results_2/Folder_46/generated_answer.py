def find_n_th_smallest_num(numbers):
    n = 4
    start_index = 36
    end_index = 93
    if len(numbers) < end_index or n > end_index - start_index + 1:
        return None
    selected_numbers = sorted(numbers[start_index:end_index + 1])
    return selected_numbers[n - 1]