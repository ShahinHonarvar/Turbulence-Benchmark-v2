def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i] == '0':
                return False
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
                return False
        return True
    x = numbers[98]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)