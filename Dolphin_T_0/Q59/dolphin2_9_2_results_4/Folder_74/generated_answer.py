def all_left_truncatable_prime(tup):
    x = tup[36]
    primes = [2, 3, 5, 7]
    for num in range(10, x):
        if all((num % i != 0 for i in range(2, num))):
            if num not in primes:
                s = str(num)
                check = True
                for i in range(len(s)):
                    if s[:i + 1] not in primes:
                        check = False
                        break
                if check:
                    primes.append(num)
    return sorted(primes)