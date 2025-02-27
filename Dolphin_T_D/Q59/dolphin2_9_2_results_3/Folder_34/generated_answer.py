def all_left_truncatable_prime(x):

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = num // 10
        return True
    result = []
    for num in range(x, 0, -1):
        if num % 10 != 0 and is_left_truncatable_prime(num):
            result.append(num)
    return result