def find_n_th_smallest_num(numbers):
    sorted_section = sorted(numbers[30:99])
    return sorted_section[4] if len(sorted_section) >= 5 else None