def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def has_left_zero(n):
        return '0' in str(n)

    def left_truncatable_prime(n):
        if n == 1:
            return False
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[38]
    numbers = []
    for i in range(x, 1, -1):
        if has_left_zero(i):
            continue
        if left_truncatable_prime(i):
            numbers.append(i)
    return sorted(numbers, reverse=True)