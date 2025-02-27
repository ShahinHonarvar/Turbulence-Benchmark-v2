def all_left_right_truncatable_prime(numbers):
    x = numbers[49]

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

    def left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left_truncated = int(str_n[i:])
            right_truncated = int(str_n[:length - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)