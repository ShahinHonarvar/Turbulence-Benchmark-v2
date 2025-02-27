def all_left_truncatable_prime(num_tuples):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(x):
        if x < 10 or x % 10 == 0:
            return False
        while not is_prime(x) or x < 2:
            return False
        x //= 10
        return is_prime(x)
    x = num_tuples[945]
    all_truncatables = []
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            all_truncatables.append(num)
    return all_truncatables