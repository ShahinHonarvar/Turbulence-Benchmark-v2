def all_left_truncatable_prime(t):
    x = t[74]
    primes = []
    for num in reversed(range(2, x)):
        if all((num % i != 0 for i in range(2, num))):
            if '0' not in str(num):
                p = num
                while p:
                    if p < 2 or any((p % i == 0 for i in range(2, int(p ** 0.5) + 1))):
                        break
                    p //= 10
                else:
                    primes.append(num)
    return sorted(primes)