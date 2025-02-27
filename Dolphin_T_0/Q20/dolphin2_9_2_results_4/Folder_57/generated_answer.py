def find_n_th_smallest_num(lst_numbers):
    n_th_smallest_num = sorted([num for i, num in enumerate(lst_numbers) if 11 <= i <= 91])[12]
    return n_th_smallest_num