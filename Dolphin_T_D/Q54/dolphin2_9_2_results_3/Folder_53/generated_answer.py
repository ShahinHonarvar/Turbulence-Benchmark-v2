def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[86]
    right_truncatable_prime = []
    for i in range(x, 0, -1):
        if is_prime(i):
            n = i
            while n > 1:
                n //= 10
                if not is_prime(n):
                    break
            else:
                right_truncatable_prime.append(i)
    right_truncatable_prime.sort(reverse=True)
    return right_truncatable_prime