def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        if not is_prime(num) or '0' in str(num):
            return False
        while num > 9:
            num = int(str(num)[1:]) if num < 100 else int(str(num)[:-1])
            if not is_prime(num):
                return False
        return True
    return sorted([num for num in range(10, n + 1) if is_left_right_truncatable_prime(num)], reverse=True)