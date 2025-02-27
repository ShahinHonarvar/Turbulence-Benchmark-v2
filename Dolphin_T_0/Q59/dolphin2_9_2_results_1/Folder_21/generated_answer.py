def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for num in range(x):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        if str(prime).count('0') == 0:
            truncation = prime
            while truncation > 0:
                if truncation in primes:
                    if truncation not in left_truncatable_primes:
                        left_truncatable_primes.append(truncation)
                    truncation = int(str(truncation)[:-1])
                else:
                    break
    left_truncatable_primes.sort()
    return left_truncatable_primes