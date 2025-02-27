def all_left_right_truncatable_prime(t):
    x = t[14]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if '0' in str(num):
            continue
        if all((int(str(num)[:i]) in primes and int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)