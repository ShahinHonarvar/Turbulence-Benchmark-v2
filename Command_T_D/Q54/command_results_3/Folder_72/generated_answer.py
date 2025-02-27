def all_right_truncatable_prime(n):
    primes = []
    for num in range(3, n[1], 2):
        if all((num % d == 0 for d in range(2, int(num ** 0.5) + 1))):
            break
        while num % 2 == 0:
            num //= 2
        while num % 5 == 0:
            num //= 5
        if num == 1:
            primes.append(num)
    return primes