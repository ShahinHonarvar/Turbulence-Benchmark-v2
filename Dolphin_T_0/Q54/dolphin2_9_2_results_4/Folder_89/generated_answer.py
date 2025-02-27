def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    x = input_tuple[97]
    result = []
    for i in range(x, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)