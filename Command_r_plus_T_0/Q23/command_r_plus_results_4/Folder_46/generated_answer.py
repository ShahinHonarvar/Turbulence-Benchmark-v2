def find_divisors_in_range(num: int) -> list[int]:
    divisors = []
    for i in range(81, 89):
        if num % i == 0:
            divisors.append(i)
    return divisors