import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sq = int(math.sqrt(n)) + 1
    for divisor in range(3, sq, 2):
        if n % divisor == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[30]
    right_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            n = number
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
                if n == 0:
                    right_truncatable_primes.append(number)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes