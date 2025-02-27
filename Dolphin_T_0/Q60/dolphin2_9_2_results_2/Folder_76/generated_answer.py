def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(x, 0, -1):
        if num not in primes and num % 10 not in {0, 2, 4, 5, 6, 8}:
            prime = True
            for p in primes:
                if num % p == 0:
                    prime = False
                    break
            if prime:
                primes.append(num)
                truncate = num
                while truncate > 9:
                    truncate = truncate // 10
                    if truncate not in primes:
                        primes.remove(num)
                        break
                else:
                    if truncate < 10 and truncate in primes:
                        result.append(num)
    return sorted(result, reverse=True)