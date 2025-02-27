def all_left_right_truncatable_prime(data):
    x = data[645]

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
        while num > 9:
            num = int(str(num)[1:])
            if not is_prime(num):
                return False
            num = int(str(num)[:-1])
            if not is_prime(num):
                return False
        return is_prime(num)
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes