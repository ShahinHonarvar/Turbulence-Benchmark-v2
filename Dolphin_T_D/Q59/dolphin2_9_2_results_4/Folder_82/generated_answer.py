def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    x = num_tuple[69]
    res = []
    for i in range(x, 1, -1):
        if is_truncatable(i):
            res.append(i)
    return res