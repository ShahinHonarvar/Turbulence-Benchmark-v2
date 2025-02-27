def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return True
    result = []
    for k in range(2, x):
        if is_prime(k) and right_truncatable(k):
            result.append(k)
    return sorted(result, reverse=True)