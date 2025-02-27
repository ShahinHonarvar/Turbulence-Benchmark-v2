def all_right_truncatable_prime(num):
    n1, n2 = num
    x = n1
    lst = []

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    for i in range(2, x):
        f = is_prime(i)
        if f:
            n = i
            while n != 0:
                if n != i and f:
                    f = is_prime(n)
                n //= 10
            if f:
                lst.append(i)
    lst.sort()
    return lst