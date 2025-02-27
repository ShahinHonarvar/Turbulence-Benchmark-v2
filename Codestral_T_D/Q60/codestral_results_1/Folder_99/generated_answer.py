def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        while num >= 10:
            num = int(str(num)[1:])
            if not is_prime(num):
                return False
        return True

    def is_right_truncatable(num):
        while num >= 10:
            num = int(str(num)[:-1])
            if not is_prime(num):
                return False
        return True
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)