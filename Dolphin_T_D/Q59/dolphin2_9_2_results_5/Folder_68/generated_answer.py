def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    prime_list = [i for i in range(2, numbers[1]) if is_prime(i) and i % 10 != 0]
    return sorted([i for i in prime_list if is_left_truncatable(i)], reverse=True)