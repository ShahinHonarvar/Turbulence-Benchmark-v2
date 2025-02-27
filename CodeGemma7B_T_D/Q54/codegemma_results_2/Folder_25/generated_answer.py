def all_right_truncatable_prime(tup):
    x = tup[92]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if not is_prime(n):
                return False
        return True
    result = [i for i in range(x) if is_prime(i) and right_truncatable(i)]
    return sorted(result)