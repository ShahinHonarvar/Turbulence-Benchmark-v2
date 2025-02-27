def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = num_tuple[71]
    prime_list = [n for n in range(2, x) if is_prime(n) and is_truncatable(n)]
    return sorted(prime_list, reverse=True)