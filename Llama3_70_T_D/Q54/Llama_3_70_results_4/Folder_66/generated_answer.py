def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[25]
    right_truncatable_primes = [i for i in range(2, x) if is_prime(i) and all((is_prime(int(str(i)[:j + 1])) for j in range(len(str(i)) - 1)))]
    return sorted(right_truncatable_primes, reverse=True)