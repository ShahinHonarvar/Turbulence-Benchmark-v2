def all_left_truncatable_prime(a):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = a[67]
    primes = []
    for num in range(x, 1, -1):
        has_zero = any((i == 0 for i in map(int, str(num))))
        if not has_zero:
            i = 0
            while True:
                left = int(''.join(str(num)[i:]))
                if left <= 1:
                    break
                if not is_prime(left):
                    break
                i += 1
            else:
                primes.append(num)
    return sorted(primes, reverse=True)