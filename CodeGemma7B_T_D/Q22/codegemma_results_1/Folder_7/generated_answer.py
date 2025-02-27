def find_sum_of_multiples(n):
    sum = 0
    for k in range(1, 417):
        if k % n == 0:
            sum += k
    return sum