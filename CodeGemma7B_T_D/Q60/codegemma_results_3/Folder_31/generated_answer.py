def all_left_right_truncatable_prime(tp):
    x = tp[50]
    if x < 2 or x % 2 == 0 or x % 5 == 0:
        return []
    primes = [2, 3, 5] + [i for i in range(7, x, 2) if all((i % j for j in range(3, int(i ** 0.5) + 1, 2)))]
    ans = []
    for i in primes:
        if '0' not in str(i):
            a, b = (str(i)[0], str(i)[-1])
            while a + b != '1' and a + b != '2' and (a + b != '5') and (a + b != '8'):
                i, a, b = (int(b), b, a + b)
                if i in primes:
                    ans.append(i)
    return sorted(ans, reverse=True)