def all_left_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = input_tuple[46]
    primes_list = sorted([n for n in range(2, x) if is_prime(n)], reverse=True)

    def is_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, 0, -1):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return [n for n in primes_list if is_truncatable_prime(n)]