def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    x = input_tuple[84]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)