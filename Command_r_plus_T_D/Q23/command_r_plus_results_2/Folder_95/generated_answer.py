def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(35, 99):
        if num % i == 0 and i <= 98 and (i >= 35):
            divisors.append(i)
    return divisors