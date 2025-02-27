def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[945]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            trunc_left = int(str_num[i:])
            trunc_right = int(str_num[:-1 - i])
            if not (is_prime(trunc_left) and is_prime(trunc_right)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)