def all_left_truncatable_prime(x):
    result = []

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    for i in range(2, x):
        if is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)