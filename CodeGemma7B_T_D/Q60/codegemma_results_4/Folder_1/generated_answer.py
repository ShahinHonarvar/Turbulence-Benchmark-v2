def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[20]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        n_str = str(n)
        for i in range(1, len(n_str)):
            left, right = (int(n_str[i:]), int(n_str[:i]))
            if not is_prime(left) or not is_prime(right):
                return False
        return is_prime(n)
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)