def all_left_truncatable_prime(x):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_str = str(n)
        if n_str[0] == '0' or not is_prime(int(n_str[1:])):
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    left_truncatable_prime_list = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_prime_list.append(i)
    return sorted(left_truncatable_prime_list, reverse=True)