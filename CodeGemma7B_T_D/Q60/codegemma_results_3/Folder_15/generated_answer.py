def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    truncated_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num) and is_prime(num):
            truncated_primes.append(num)
    if not truncated_primes:
        return []
    return sorted(truncated_primes, reverse=True)