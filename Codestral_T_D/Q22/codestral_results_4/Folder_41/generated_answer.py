def find_sum_of_multiples(n: int) -> int:
    return sum((n * i for i in range(1, 64)))