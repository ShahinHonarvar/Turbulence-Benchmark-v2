def find_n_th_smallest_num(numbers):
    indexed_numbers = enumerate(numbers)
    sorted_numbers = sorted(indexed_numbers)[23:58]
    fourth_smallest_num = sorted_numbers[3][1]
    return fourth_smallest_num