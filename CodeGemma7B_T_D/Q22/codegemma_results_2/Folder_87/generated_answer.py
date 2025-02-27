def find_sum_of_multiples(x):
    z = 0
    for i in range(1, 115):
        if i % x == 0:
            z += i
    return z