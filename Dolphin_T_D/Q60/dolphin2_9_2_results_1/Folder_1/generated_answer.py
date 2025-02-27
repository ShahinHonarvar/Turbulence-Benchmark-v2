def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            if is_prime(n_str[1:]) and is_prime(int(n_str[:len(n_str) - 1])):
                n_str = n_str[1:-1]
            else:
                return False
        return True
    x = t[20]
    prime_list = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            prime_list.append(i)
    if len(prime_list) == 0:
        return []
    else:
        return sorted(prime_list, reverse=True)