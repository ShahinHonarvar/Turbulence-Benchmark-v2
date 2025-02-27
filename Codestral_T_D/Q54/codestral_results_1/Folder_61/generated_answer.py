def all_right_truncatable_prime(t):
    x = t[3]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    if x < 2:
        return right_truncatable_primes
    for num in range(11, x):
        if all((num % p != 0 for p in primes)) and all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))):
            right_truncatable_primes.append(num)
            primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes