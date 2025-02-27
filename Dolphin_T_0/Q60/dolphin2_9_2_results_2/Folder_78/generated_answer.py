def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                return False
        return True

    def left_right_truncatable(num):
        for x in range(2, len(str(num))):
            if not is_prime(int(str(num)[x:-x] or '0')):
                return False
        return True
    return sorted({n for n in range(2, x + 1) if left_right_truncatable(n)})