def all_right_truncatable_prime(tuple_input):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tuple_input[70]
    result = []
    for num in range(x - 1, 1, -1):
        if is_right_truncatable_prime(num):
            result.append(num)
    return result