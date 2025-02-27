def all_left_truncatable_prime(x):

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n) and n != 0
        else:
            return is_prime(n) and n % 10 != 0 and is_left_truncatable_prime(n // 10)

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    result = []
    for n in range(x, 1, -1):
        if is_left_truncatable_prime(n):
            result.append(n)
    return result