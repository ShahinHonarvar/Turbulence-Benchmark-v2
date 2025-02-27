def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[758]
    prime = []
    for i in range(1, x):
        if is_prime(i):
            p = i
            while p > 0:
                if not is_prime(p):
                    break
                p //= 10
            else:
                prime.append(i)
    return sorted(prime)