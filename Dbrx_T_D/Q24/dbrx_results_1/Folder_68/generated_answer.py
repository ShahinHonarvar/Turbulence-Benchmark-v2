def sum_of_divisors_in_range(n: int) -> int:
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        if 3 <= i <= 6:
            divisors_sum += i
    return divisors_sum if divisors_sum > 0 else 0