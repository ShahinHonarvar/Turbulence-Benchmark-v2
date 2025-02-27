def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(4, 9):
        if num % i == 0:
            divisors.append(i)
    return divisors