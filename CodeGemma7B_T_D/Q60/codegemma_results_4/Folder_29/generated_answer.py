def all_left_right_truncatable_prime(x):
    x = x[55]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            left_num = int(str_num[:i])
            right_num = int(str_num[i:])
            if not (is_prime(left_num) and is_prime(right_num)):
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes