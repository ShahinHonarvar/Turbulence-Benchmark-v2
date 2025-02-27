def all_left_truncatable_prime(numbers):
    x = numbers[87]
    primes = [2]
    trunc_primes = []
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
            num = i
            while num:
                num //= 10
                if num < i and num not in primes:
                    break
            else:
                trunc_primes.append(i)
    return sorted(trunc_primes)