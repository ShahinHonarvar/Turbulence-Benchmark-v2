def all_right_truncatable_prime(x):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        n = len(str(num))
        while n > 1:
            if not is_prime(int(str(num)[-n:])):
                return False
            n -= 1
        return True
    return sorted([i for i in range(x - 1, 0, -1) if is_truncatable_prime(i)], reverse=False)