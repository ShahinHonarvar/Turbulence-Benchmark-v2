def all_left_right_truncatable_prime(integers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = integers[19]
    primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        is_truncatable = True
        n = i
        while n > 1:
            if not is_prime(n):
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            primes.append(i)
    return sorted(primes)