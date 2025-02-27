def all_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:i + 1])):
                return False
        return True
    limit = args[0]
    return sorted([i for i in range(2, limit) if is_right_truncatable_prime(i)], reverse=True)