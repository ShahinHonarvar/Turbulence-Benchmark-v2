def find_sum_of_multiples(n):
    sum = 0
    for i in range(n, 52 * n + 1, n):
        sum += i
    return sum