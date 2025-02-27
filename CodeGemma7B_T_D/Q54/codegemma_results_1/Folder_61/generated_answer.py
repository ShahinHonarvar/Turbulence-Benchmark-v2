def all_right_truncatable_prime(x):

    def is_prime(n):
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for digit in str_n[:-1]:
            n = int(str_n[:-1])
            if not is_prime(n):
                return False
            str_n = str_n[:-1]
        return is_prime(n)
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)