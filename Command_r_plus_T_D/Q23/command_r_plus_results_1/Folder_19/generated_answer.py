def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(1, 8):
        if num % i == 0:
            divisors.append(i)
    return divisors