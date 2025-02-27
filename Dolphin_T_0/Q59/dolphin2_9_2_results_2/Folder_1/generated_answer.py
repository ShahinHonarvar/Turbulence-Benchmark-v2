def all_left_truncatable_prime(in_tuple):

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_left_truncatable(n):
        if '0' in str(n):
            return False
        while n != 0:
            if not check_prime(n):
                return False
            n //= 10
        return True
    x = in_tuple[20]
    result = []
    for i in reversed(range(2, x)):
        if check_left_truncatable(i):
            result.append(i)
    return result