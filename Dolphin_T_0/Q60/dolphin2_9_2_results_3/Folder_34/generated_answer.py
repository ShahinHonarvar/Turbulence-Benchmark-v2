def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[18]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if '0' not in str(num) and all((is_prime(int(str(num)[i:j])) for i in range(0, -len(str(num)), -1) for j in range(-i, 0))):
            primes.append(num)
    return sorted(primes, reverse=True)