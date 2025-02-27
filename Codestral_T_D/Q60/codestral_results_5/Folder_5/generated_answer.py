def all_left_right_truncatable_prime(t):
    x = t[55]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:]) if n >= 10 else 0

    def truncate_right(n):
        return int(str(n)[:-1])
    lrt_primes = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        num = n
        while num > 0:
            if not is_prime(num):
                break
            num = truncate_left(num)
        if num > 0:
            continue
        num = n
        while num > 0:
            if not is_prime(num):
                break
            num = truncate_right(num)
        if num == 0:
            lrt_primes.append(n)
    return sorted(lrt_primes)