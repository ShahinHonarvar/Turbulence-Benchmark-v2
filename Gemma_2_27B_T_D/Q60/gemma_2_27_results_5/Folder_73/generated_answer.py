def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncable = True
            n = str(num)
            while len(n) > 1:
                n = n[1:]
                if not is_prime(int(n)):
                    truncable = False
                    break
            n = str(num)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    truncable = False
                    break
            if truncable:
                primes.append(num)
    return sorted(primes)