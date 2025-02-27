def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    if not is_prime(n):
        for i in range(59, 89):
            if n % i == 0:
                sum_of_divisors += i
    return sum_of_divisors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True