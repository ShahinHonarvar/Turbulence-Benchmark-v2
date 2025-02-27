def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 2:
            return False
        num = n
        while num != 0:
            if is_prime(num):
                num //= 10
        return num == 0
    x = t[30]
    prime = []
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            prime.append(i)
    prime.sort()
    return prime