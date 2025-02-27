def all_left_right_truncatable_prime(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if not is_prime(int(n_str[i + 1:])) or not is_prime(int(n_str[:i])):
                return False
        return True
    x = num_list[767]
    left_right_truncatable_primes = [i for i in range(x, 1, -1) if is_truncatable(i) and is_prime(i)]
    return left_right_truncatable_primes