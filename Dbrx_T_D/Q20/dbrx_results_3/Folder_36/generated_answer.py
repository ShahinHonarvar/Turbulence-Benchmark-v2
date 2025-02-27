def find_n_th_smallest_num(numbers):
    n = 5
    target_indices = list(range(291, 313))
    target_numbers = [numbers[i] for i in target_indices]
    sorted_numbers = sorted(target_numbers)
    return sorted_numbers[n - 1]