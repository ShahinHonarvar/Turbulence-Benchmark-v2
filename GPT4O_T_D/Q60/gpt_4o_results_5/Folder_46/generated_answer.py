def all_left_right_truncatable_prime(numbers):
    x = numbers[33]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def has_no_zero(n):
        return '0' not in str(n)

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(length):
            left_truncated = int(str_n[i:])
            right_truncated = int(str_n[:length - i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and has_no_zero(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)