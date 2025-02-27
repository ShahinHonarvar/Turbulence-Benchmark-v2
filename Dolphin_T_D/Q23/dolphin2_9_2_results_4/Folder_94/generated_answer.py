def find_divisors_in_range(n: int) -> list:
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return [x for x in divisors if 35 <= x <= 37]