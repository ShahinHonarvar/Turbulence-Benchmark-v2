def find_divisors_in_range(n: int) -> list[int]:
    divisors = []
    for divisor in range(1, 8):
        if n % divisor == 0:
            divisors.append(divisor)
    return divisors