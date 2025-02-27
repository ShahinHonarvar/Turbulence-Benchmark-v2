def sum_even_ints_inclusive(num_list):
    sum_evens = 0
    for i in range(75, 95):
        if num_list[i] % 2 == 0:
            sum_evens += num_list[i]
    return sum_evens or 0