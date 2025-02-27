def all_right_truncatable_prime(ints):
    x = ints[19]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            truncatable = True
            n = num
            while n > 0:
                if n < 2 or n % 2 == 0:
                    truncatable = False
                    break
                divisible = False
                for i in range(3, int(n ** 0.5) + 1, 2):
                    if n % i == 0:
                        divisible = True
                        break
                if divisible:
                    truncatable = False
                    break
                n //= 10
            if truncatable:
                primes.append(num)
    return sorted(primes)