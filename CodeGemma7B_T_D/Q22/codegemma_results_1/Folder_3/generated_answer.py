def find_sum_of_multiples(int_a):
    sum_a = 0
    for i in range(92):
        sum_a += (i + 1) * int_a
    return sum_a