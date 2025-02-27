from itertools import count

def all_right_truncatable_prime(t):
    x = t[7]

    def is_prime(n):
        if n < 2:
            return False
        for i in count(2, 1):
            if n % i == 0:
                return False
            if i * i > n:
                break
        return True
    c = 1
    list_0 = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n % 10 != 0 and n > 0:
                if is_prime(n):
                    c += 1
                    list_0.append(n)
                n //= 10
    list_0.sort()
    return list_0