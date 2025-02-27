def find_sum_of_multiples(n: int) -> int:
    return sum(range(n, 59 * n + 1, n))