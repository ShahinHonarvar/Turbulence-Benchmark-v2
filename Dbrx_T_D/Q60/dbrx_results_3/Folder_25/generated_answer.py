def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 9:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return is_prime(num)
    x = sorted(set(n))[92]
    return [i for i in range(1, x + 1) if is_left_right_truncatable_prime(i)]