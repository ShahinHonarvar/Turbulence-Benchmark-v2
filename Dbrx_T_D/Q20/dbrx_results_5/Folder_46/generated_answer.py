def find_n_th_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 36:
        return None
    sub_numbers = sorted(numbers[36:94])
    if len(sub_numbers) < 4:
        return None
    return sub_numbers[3]