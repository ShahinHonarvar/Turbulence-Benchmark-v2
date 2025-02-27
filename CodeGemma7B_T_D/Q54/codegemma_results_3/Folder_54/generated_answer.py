def all_right_truncatable_prime(x):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        return True
    result = [i for i in range(x) if right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result or []