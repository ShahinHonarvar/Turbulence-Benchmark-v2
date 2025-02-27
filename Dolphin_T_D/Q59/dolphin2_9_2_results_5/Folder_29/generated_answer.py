def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_truncatable_prime(n):
        n = str(n)
        while n:
            if n[0] == '0':
                return False
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True
    x = t[55]
    result = []
    for i in reversed(range(2, x)):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result