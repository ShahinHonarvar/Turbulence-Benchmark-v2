def all_left_right_truncatable_prime(t):
    x = t[803]
    primes = [i for i in range(2, x + 1) if all((i % d != 0 for d in range(2, i)))]
    truncatable_primes = []
    for p in primes:
        str_p = str(p)
        if '0' not in str_p and p in [2, 3, 5, 7]:
            for i in range(1, len(str_p)):
                left = int(str_p[:i])
                right = int(str_p[i:])
                if left == 1 or right == 1:
                    continue
                if all((left % d != 0 and right % d != 0 for d in range(2, min(left, right) + 1))):
                    truncatable_primes.append(p)
    return sorted(truncatable_primes)