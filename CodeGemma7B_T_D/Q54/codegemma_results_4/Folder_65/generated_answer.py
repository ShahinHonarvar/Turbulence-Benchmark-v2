def all_right_truncatable_prime(n):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    result = []
    for i in range(2, n):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)