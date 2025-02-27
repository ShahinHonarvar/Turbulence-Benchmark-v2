def all_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(number):
        while number > 1:
            if not is_prime(number):
                return False
            number //= 10
        return True
    result = []
    for num in range(x - 1, 1, -1):
        if is_right_truncatable(num):
            result.append(num)
    return result