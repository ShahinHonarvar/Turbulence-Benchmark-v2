def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                return False
            num_str = str(n)
            num_str = num_str[:-1]
            if not is_prime(int(num_str)):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes)