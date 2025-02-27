def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime = []
    truncatable = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime.append(i)
    for i in prime:
        a = str(i)
        if '0' not in a:
            b = a[1:]
            while b:
                if b in prime and int(b) in prime:
                    truncatable.append(i)
                b = b[:-1]
    return sorted(truncatable, reverse=True)