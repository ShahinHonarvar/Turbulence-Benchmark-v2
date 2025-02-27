def all_right_truncatable_prime(t):
    x = t[98]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            if all((int(str_num[i:]) in primes for i in range(1, len(str_num)))):
                primes.append(num)
    return sorted(primes)