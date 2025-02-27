def find_sum_of_multiples(n):
    sum = 0
    for i in range(n, 65 * n + n, n):
        sum += i
    return sum