def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tup[41]
    res_list = [i for i in range(x) if is_prime(i) and is_truncatable(i)]
    return sorted(res_list)