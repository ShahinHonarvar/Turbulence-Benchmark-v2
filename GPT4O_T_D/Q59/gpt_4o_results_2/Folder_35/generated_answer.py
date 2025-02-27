def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(prime):
    str_prime = str(prime)
    if '0' in str_prime:
        return False
    for i in range(len(str_prime)):
        if not is_prime(int(str_prime[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    left_truncatable_primes = []
    for number in range(2, x):
        if is_prime(number) and left_truncatable(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes