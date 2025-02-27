def all_left_right_truncatable_prime(x):
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        if '0' in str(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[1:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return result