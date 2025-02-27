def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x + 1):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    filtered_primes = [p for p in primes if '0' not in str(p)]

    def is_truncatable_prime(p):
        str_p = str(p)
        for i in range(1, len(str_p)):
            left = int(str_p[i:])
            right = int(str_p[:-i])
            if left <= 1 or right <= 1 or left % 2 == 0 or (right % 2 == 0) or (left not in primes) or (right not in primes):
                return False
        return True
    truncatable_primes = sorted([p for p in filtered_primes if is_truncatable_prime(p)], reverse=True)
    return truncatable_primes or []