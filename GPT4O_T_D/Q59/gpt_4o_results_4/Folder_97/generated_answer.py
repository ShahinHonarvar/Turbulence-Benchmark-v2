def all_left_truncatable_prime(numbers):
    x = numbers[645]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)