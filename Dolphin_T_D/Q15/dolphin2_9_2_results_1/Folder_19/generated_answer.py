def sum_odd_ints_inclusive(num_list):
    x = sum([num for i, num in enumerate(num_list[3:6]) if num % 2 != 0])
    return x