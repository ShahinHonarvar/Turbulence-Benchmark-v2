def all_left_truncatable_prime(x):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def helper(n):
        result = []
        for i in range(2, n):
            if is_prime(i) and is_truncatable_prime(i):
                result.append(i)
        return result
    return helper(x)