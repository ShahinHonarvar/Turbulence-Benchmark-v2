def find_n_th_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        return sorted(numbers[:7])[6]