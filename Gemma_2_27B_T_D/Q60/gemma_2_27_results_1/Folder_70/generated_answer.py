def all_left_right_truncatable_prime(data):
    x = data[433]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return is_prime(int(num_str))
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes