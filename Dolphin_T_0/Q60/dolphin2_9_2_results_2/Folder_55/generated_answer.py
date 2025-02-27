def all_left_right_truncatable_prime(t):
    x, *_ = t
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    left_right_truncatable = [i for i in primes if str(i).replace('0', '').isdigit() and all(int(str(i).replace(str(i)[0], '', 1)) in primes and int(str(i).replace(str(i)[-1], '', 1)) in primes and (int(str(i).replace(str(i)[:2], '', 1)) in primes) and (int(str(i).replace(str(i)[-2:], '', 1)) in primes))]
    return sorted(left_right_truncatable, reverse=True)