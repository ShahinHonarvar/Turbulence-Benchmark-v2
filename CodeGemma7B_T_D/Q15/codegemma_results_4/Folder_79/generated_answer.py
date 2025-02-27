def sum_odd_ints_inclusive(num_list):
    if not num_list or len(num_list) < 5:
        return 0
    sum_odd = 0
    for i in range(4, len(num_list) + 1):
        if i % 2 == 1:
            sum_odd += i
    return sum_odd