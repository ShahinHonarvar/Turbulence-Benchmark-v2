def all_left_right_truncatable_prime(data):
    x = data[945]
    primes = [2, 3, 5, 7]
    for i in range(8, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        if p < 10:
            truncatable_primes.append(p)
            continue
        p = str(p)
        is_truncatable = True
        while len(p) > 1:
            p = p[1:]
            if int(p) not in primes:
                is_truncatable = False
                break
            p = p[:-1]
            if int(p) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(int(p))
    truncatable_primes.sort(reverse=True)
    return truncatable_primes