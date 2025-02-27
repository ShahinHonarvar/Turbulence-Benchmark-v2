def find_n_th_smallest_num(numbers):
    if len(numbers) < 91:
        return None
    sub_numbers = numbers[10:92]
    sorted_sub_numbers = sorted(sub_numbers)
    return sorted_sub_numbers[13]