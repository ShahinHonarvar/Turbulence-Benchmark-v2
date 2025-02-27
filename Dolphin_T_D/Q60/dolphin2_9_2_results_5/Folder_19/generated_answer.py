def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or n < 100:
            return False
        left_str = str(n)[1:-1]
        right_str = str(n)[1:]
        return is_truncatable(int(left_str)) and is_truncatable(int(right_str))
    primes = []
    for num in range(num_tuple[67], 0, -1):
        if is_truncatable(num) and is_prime(num):
            primes.append(num)
    return primes