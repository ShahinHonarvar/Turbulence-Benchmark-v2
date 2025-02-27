def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(10, 70):
        if num % i == 0:
            divisors.append(i)
    return divisors