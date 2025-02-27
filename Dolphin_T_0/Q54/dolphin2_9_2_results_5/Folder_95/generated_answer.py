def all_right_truncatable_prime(t):
    primes = []
    for num in range(2, t[77]):
        if all((num % i != 0 for i in range(2, num))):
            right_truncatable = True
            n = num
            while n > 1:
                if all((n % i != 0 for i in range(2, n))):
                    n //= 10
                else:
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(num)
    return sorted(primes)