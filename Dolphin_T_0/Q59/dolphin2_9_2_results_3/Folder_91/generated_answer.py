def all_left_truncatable_prime(tup):

    def is_left_truncatable_prime(n):
        if n == 0:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(num):
        if num == 1 or num == 0:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    x = tup[0]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(result, reverse=True)