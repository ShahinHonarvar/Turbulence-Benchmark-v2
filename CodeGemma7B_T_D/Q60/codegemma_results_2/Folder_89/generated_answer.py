def all_left_right_truncatable_prime(x):
    ans = []

    def isprime(n):
        if n <= 1:
            return False
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def leftprime(n):
        while n > 1:
            if not isprime(n):
                return False
            n //= 10
        return True

    def rightprime(n):
        while n >= 1:
            if not isprime(n):
                return False
            n //= 10
        return True
    for i in range(x, 0, -1):
        a = i
        if isprime(i):
            a //= 10
            if leftprime(a):
                b = a
                while True:
                    temp = b % 10
                    if temp == 0:
                        b //= 10
                        continue
                    if not isprime(b):
                        break
                    b //= 10
                    if rightprime(b):
                        ans.append(i)
                        break
    return sorted(ans, reverse=True)