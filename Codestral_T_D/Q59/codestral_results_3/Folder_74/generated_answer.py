def all_left_truncatable_prime(args):
    x = args[36]
    primes = [2]
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        num = prime
        while num:
            if num not in primes:
                break
            num //= 10
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)