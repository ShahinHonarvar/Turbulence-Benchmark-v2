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

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            left_truncate = int(str_num[i:]) if i < length else 0
            right_truncate = int(str_num[:length - i]) if i < length else 0
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                return False
        return True
    if len(numbers) <= 43:
        return []
    x = numbers[43]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)