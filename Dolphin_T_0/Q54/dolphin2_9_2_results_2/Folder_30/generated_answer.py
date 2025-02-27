def all_right_truncatable_prime(t):
    x = t[37]
    primes = [2, 3, 5, 7]
    for num in range(10, x):
        if all((num % i != 0 for i in range(2, num))):
            if all((int(str(num)[i:]) % i != 0 for i in range(1, str(num)[::-1].find('0')))):
                primes.append(num)
    return sorted(primes, reverse=True)