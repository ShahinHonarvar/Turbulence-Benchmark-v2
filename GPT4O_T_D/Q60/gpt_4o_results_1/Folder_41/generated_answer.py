def all_left_right_truncatable_prime(numbers):
    x = numbers[46]

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

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:length - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    left_right_truncatable_primes = []
    for n in range(x + 1):
        if is_prime(n) and is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes, reverse=True)