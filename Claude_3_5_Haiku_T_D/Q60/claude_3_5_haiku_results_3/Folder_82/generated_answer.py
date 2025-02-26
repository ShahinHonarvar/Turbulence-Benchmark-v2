def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[69]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[1:]
            left_trunc = int(str_num)
            right_trunc = int(str(num)[:-len(str_num)])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes