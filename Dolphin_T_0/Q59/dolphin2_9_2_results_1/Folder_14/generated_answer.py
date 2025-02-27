def all_left_truncatable_prime(num_tuple):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        i = n
        while i > 1:
            if i % 10 == 0:
                return False
            if not is_prime(i):
                return False
            i //= 10
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[78]
    result = [i for i in range(x, 0, -1) if is_left_truncatable_prime(i)]
    return result