def all_left_right_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while len(str(n)) > 1:
            left, right = (n // 10 ** len(str(n)), n % 10)
            n = n % 10 ** len(str(n)) - right
            if not is_prime(left) or not is_prime(right) or (not is_truncatable_prime(n // 10)):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result)