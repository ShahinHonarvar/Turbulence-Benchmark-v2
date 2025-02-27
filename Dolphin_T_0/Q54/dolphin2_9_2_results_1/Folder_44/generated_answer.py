def all_right_truncatable_prime(n):

    def is_prime(m):
        if m <= 1:
            return False
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True
    primes = [2]
    for p in range(3, n):
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
    right_truncatable = [p for p in primes if all(is_prime((''.join(map(str, [int(d) for d in str(p).rstrip(str(p)[-1])])) for _ in range(1, len(str(p))))))]
    return sorted(right_truncatable)