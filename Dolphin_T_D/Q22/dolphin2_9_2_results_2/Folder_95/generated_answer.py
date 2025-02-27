def find_sum_of_multiples(n: int) -> int:
    return sum((n * k for k in range(1, 89)))