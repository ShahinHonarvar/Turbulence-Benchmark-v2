def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n <= 11:
            return False
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(1, length):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)