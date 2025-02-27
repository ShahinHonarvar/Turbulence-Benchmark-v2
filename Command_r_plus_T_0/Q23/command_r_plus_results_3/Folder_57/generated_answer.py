def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(15, 93):
        if num % i == 0:
            divisors.append(i)
    return divisors