def find_divisors_in_range(n: int) -> list[int]:
    divisors = []
    for divisor in range(50, 82):
        if n % divisor == 0:
            divisors.append(divisor)
    return divisors