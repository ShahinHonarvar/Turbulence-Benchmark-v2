def all_left_right_truncatable_prime(t):
    x = t[98]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) is not None and int(str(num)[:i]) > 1 and (sum((int(d) for d in str(int(str(num)[:i])))) % 100 != 0) for i in range(1, len(str(num)) + 1))) and all((int(str(num)[i:]) is not None and int(str(num)[i:]) > 1 and (sum((int(d) for d in str(int(str(num)[i:])))) % 100 != 0) for i in range(len(str(num))))):
            isPrime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    isPrime = False
                    break
            if isPrime and '0' not in str(num):
                primes.append(num)
    return sorted(primes)