def left_right_truncatable_prime(n):

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
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:]) if num < 10 else int(str(num)[:-1])
        return True
    return [i for i in range(2, n + 1) if is_left_right_truncatable_prime(i)]

def all_left_right_truncatable_prime(t):
    return sorted([x for x in left_right_truncatable_prime(t[81]) if x <= t[81]], reverse=True)