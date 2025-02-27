def all_left_right_truncatable_prime(numbers):
    x = numbers[31]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    truncatable_primes = [num for num in range(2, x + 1) if is_prime(num) and is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)