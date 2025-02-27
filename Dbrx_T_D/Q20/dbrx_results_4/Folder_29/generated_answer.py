def find_n_th_smallest_num(numbers):
    if len(numbers) < 63:
        return None
    selected_numbers = numbers[20:63]
    selected_numbers.sort()
    return selected_numbers[11]