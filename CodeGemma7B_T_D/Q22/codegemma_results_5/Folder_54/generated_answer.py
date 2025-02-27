def find_sum_of_multiples(n):
    return sum((x for x in range(1, 30) if x % n == 0))