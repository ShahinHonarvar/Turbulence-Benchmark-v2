def find_divisors_in_range(num: int) -> list[int]:
    divisors = [i for i in range(10, 56) if num % i == 0]
    return divisors