def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if n_str[i] == '0':
                return False
            if not is_prime(int(n_str[i:])):
                return False
        return True
    left_truncatable_prime_list = []
    for n in range(2, x):
        if is_truncatable_prime(n):
            left_truncatable_prime_list.append(n)
    left_truncatable_prime_list.sort()
    return left_truncatable_prime_list