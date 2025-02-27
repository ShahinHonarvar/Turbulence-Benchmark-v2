def find_n_th_smallest_num(numbers: list[int]) -> int:
    start_index = 11
    end_index = 24
    n_th_smallest = 10
    if not numbers or len(numbers) < end_index:
        raise ValueError('Input list must have at least 24 elements.')
    sorted_numbers = sorted(numbers[start_index:end_index])
    return sorted_numbers[n_th_smallest - 1]