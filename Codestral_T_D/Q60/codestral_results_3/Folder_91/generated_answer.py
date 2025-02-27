def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    x = numbers[0]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_truncatable_prime(n) and is_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes