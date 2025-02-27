def all_left_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        if len(n_str) == 1:
            return True
        if not is_prime(int(n_str[1:])) or not is_prime(int(n_str[:-1])):
            return False
        return is_truncatable(int(n_str[1:])) and is_truncatable(int(n_str[:-1]))
    x = n_tuple[41]
    result = [i for i in range(2, x + 1) if is_truncatable(i)]
    return sorted(result, reverse=True)