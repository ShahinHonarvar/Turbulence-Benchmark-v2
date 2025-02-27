def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def is_truncatable_prime(n):
    n = str(n)
    return all((is_prime(int(n[-i:])) for i in range(1, len(n))))

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(primes)