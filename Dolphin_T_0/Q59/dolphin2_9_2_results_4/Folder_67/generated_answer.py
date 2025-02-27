def all_left_truncatable_prime(my_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    x = my_tuple[71]
    return sorted([i for i in range(x - 1, 0, -1) if is_left_truncatable_prime(i)], reverse=True)