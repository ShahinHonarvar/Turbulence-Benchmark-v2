def all_left_right_truncatable_prime(argtuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n <= 1 or '0' in str(n) or (not is_prime(n)):
            return False
        while len(str(n)) > 1:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    x = argtuple[87]
    result = []
    for i in range(x + 1):
        if is_truncatable(i):
            result.append(i)
    return result