def all_left_truncatable_prime(t):
    x = t[91]

    def left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if t[i] == '0':
            continue
        if left_truncatable(i):
            result.append(i)
    return sorted(result)