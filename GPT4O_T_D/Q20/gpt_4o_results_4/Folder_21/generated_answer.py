def find_n_th_smallest_num(numbers):
    if len(numbers) < 636:
        return None
    sublist = sorted(numbers[299:636])
    return sublist[11]