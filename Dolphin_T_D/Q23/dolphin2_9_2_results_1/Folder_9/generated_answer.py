def find_divisors_in_range(number: int) -> list:
    divisors = []
    for divisor in range(3, 10):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors