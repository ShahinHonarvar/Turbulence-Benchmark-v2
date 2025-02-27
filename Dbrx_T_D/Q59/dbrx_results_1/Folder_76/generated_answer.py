def all_left_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers_tuple[370]
    return sorted([i for i in range(2, x) if is_left_truncatable(i)], reverse=True)