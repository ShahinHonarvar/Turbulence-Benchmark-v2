def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            prime = i
            while prime:
                if is_prime(prime):
                    prime //= 10
                else:
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)