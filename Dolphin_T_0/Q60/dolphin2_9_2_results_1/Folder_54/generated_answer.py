def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        for i in range(1, len(str(n)) - 1):
            if not is_prime(n):
                return False
            n = n // 10
            if not is_prime(n):
                return False
        return True
    prime_list = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            prime_list.append(n)
    return prime_list