def find_divisors_in_range(num: int) -> list:
    divisors = []
    for divisor in range(157, 903):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors