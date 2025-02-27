def find_n_th_smallest_num(numbers):
    n = 5
    sub_numbers = numbers[13:41]
    sorted_numbers = sorted(sub_numbers)
    if len(sorted_numbers) >= n:
        return sorted_numbers[n - 1]
    else:
        return None