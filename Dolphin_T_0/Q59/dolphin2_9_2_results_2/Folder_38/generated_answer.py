def all_left_truncatable_prime(t):
    x = t[28]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        while n:
            if n[0] == '0' or not is_prime(int(n)):
                return False
            n = n[1:]
        return True
    result = []
    for num in range(2, x):
        if is_left_truncatable(num):
            result.append(num)
    return result