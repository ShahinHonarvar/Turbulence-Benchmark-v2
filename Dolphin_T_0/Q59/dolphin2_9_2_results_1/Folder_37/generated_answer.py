def all_left_truncatable_prime(num_tuple):
    x = num_tuple[35]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n < 2:
            return False
        n_str = str(n)
        for i in range(len(n_str)):
            if int(n_str[i:]) % 10 == 0:
                return False
            if not is_prime(int(n_str[i:])):
                return False
        return True
    result = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable(i) and is_prime(i):
            result.append(i)
    return sorted(result, reverse=True)