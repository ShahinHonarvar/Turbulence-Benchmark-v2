def all_left_truncatable_prime(tup):
    x = tup[39]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    l = []
    for num in range(2, x):
        if is_prime(num):
            n = num
            while n != 0:
                if n != num and (not is_prime(n)):
                    break
                n //= 10
            else:
                l.append(num)
    return sorted(l)