def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(40, 75):
        if num % i == 0:
            divisors.append(i)
    return divisors