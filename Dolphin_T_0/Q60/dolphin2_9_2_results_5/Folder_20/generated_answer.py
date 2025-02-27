def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def trunc_prime(n):
        while n > 9:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    result = []
    for n in range(x, 100, -1):
        if trunc_prime(n) and is_prime(n):
            result.append(n)
    return result