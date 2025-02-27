def find_n_th_smallest_num(numbers):
    return sorted(numbers[30:99])[5] if len(numbers) > 5 and len(numbers) > 98 else None