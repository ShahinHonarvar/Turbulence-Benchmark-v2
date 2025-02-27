def all_left_right_truncatable_prime(x):

    def _is_truncatable_prime(n):
        if not str(n).replace('0', '').isnumeric() or not is_prime(n):
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[:-i - 1])):
                return False
            if not is_prime(int(str(n)[i + 1:])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if _is_truncatable_prime(i):
            result.append(i)
    if not result:
        return []
    return sorted(result, reverse=True)