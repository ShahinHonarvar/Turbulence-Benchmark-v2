def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[81]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)