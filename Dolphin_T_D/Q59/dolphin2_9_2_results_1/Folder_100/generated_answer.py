def all_left_truncatable_prime(x):

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

    def is_left_truncatable_prime(n):
        if n <= 1 or n % 10 == 0:
            return False
        while n != 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    result = []
    for i in range(2, min(x, 10)):
        if is_left_truncatable_prime(i):
            result.append(i)
    length = len(str(x))
    for i in range(10, 10 ** length):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)