def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    primes = []
    for i in range(10 ** len(str(num)) - 1, 0, -1):
        if is_prime(i) and is_prime(i // 10):
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:
    threshold = numbers[760]
    trunc_primes = right_truncatable_primes(threshold)
    return sorted(trunc_primes, reverse=True)