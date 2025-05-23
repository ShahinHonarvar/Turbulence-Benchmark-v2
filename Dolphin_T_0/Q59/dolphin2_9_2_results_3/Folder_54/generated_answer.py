def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable(i):
            result.append(i)
    result.sort(reverse=True)
    return result