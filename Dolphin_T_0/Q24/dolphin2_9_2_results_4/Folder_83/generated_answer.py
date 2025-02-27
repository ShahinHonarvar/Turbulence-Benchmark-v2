def sum_of_divisors_in_range(k):
    sum_k = 0
    if k % 2 != 0:
        return 0
    else:
        for i in range(5, 8):
            if k % i == 0:
                sum_k += k / i
    return sum_k