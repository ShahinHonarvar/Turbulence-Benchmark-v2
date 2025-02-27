def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        while n:
            if n % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True
    numbers = []
    for i in range(10, x):
        if is_truncatable(i):
            numbers.append(i)
    return sorted(numbers)