def find_n_th_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        first_five_smallest = sorted(numbers[:5])
        return first_five_smallest[4]