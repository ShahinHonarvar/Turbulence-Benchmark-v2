def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 40:
        return []
    x = numbers[39]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n or not is_prime(n):
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    truncatable_primes = [num for num in range(10, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)