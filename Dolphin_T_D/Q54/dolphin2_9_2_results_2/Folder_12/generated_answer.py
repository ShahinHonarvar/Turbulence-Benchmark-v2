def all_right_truncatable_prime(num_tuple):

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_right_truncatable(n):
        if not check_prime(n):
            return False
        New = n
        while True:
            New = New // 10
            if New == 0:
                return True
            if not check_prime(New):
                return False
    x = num_tuple[70]
    primes = []
    for y in range(x - 1, 1, -1):
        if check_right_truncatable(y):
            primes.append(y)
    return sorted(primes, reverse=True)