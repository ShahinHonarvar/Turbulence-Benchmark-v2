def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_trunc_primes = []
    for p in primes:
        num = p
        while num:
            if not is_prime(num):
                break
            num //= 10
        else:
            left_trunc_primes.append(p)
    return sorted(left_trunc_primes, reverse=True)