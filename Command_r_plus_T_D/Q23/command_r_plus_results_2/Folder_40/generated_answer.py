def find_divisors_in_range(num: int) -> list[int]:
    divisors = [i for i in range(1, 3) if num % i == 0]
    return divisors