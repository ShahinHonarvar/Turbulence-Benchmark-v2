def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(n, 0, -1):
        if is_prime(i):
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[37]
    primes = right_truncatable_primes(x)
    right_truncatable_primes_list = []
    for prime in primes:
        truncated_prime = str(prime)
        while len(truncated_prime) > 1:
            truncated_prime = truncated_prime[:-1]
            if not is_prime(int(truncated_prime)):
                break
        else:
            right_truncatable_primes_list.append(prime)
    return sorted(right_truncatable_primes_list, reverse=True)