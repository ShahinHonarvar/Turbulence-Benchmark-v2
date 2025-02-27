def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in range(29, 80):
        if i % 2 != 0:
            sum += num_list[i]
    return sum if sum > 0 else 0