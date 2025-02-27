def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:-i or None])):
                return False
        return True
    x = numbers[945]
    truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)