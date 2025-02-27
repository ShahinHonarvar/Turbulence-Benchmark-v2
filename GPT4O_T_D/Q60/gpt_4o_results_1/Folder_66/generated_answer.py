def all_left_right_truncatable_prime(numbers):

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

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:len(str_num) - i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                return False
        return True
    x = numbers[25]
    truncatable_primes = [n for n in range(11, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)