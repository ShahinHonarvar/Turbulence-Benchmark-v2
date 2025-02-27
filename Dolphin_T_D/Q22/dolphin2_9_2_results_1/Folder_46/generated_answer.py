def find_sum_of_multiples(n):
    *sum, i = (0, 1)
    while len(sum) < 464:
        *sum, i = (sum + i * n, i + 1)
    return sum[-1] + sum[-2]