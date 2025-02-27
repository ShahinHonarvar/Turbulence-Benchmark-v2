def all_left_right_truncatable_prime(t):
    x = t[645]
    primes = []
    for i in range(2, x + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            s = str(i)
            while len(s) > 1:
                s = s[1:]
                if int(s) not in primes:
                    break
                s = str(i)
                while len(s) > 1:
                    s = s[:-1]
                    if int(s) not in primes:
                        break
                else:
                    primes.append(i)
    return sorted(primes)