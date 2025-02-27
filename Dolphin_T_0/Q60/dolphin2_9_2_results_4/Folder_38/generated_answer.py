def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        n = str(n)
        if len(n) <= 2:
            return n.isdigit() and all((is_prime(int(n[i:j + 1])) for i in range(len(n)) for j in range(i, len(n))))
        else:
            return is_truncatable_prime(n[:-1]) and is_truncatable_prime(n[1:])

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[28]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    return [i for i in primes if is_truncatable_prime(i)]