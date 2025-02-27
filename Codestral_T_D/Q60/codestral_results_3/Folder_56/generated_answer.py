def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        truncated_num = n
        while truncated_num >= 10:
            truncated_num //= 10
            if not is_prime(truncated_num):
                return False
        truncated_num = n
        while truncated_num >= 10:
            truncated_num %= 10 ** (len(str(truncated_num)) - 1)
            if not is_prime(truncated_num):
                return False
        return True
    x = numbers[30]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)