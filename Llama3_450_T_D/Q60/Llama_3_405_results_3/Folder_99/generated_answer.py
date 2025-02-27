def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1):
                left_trunc = int(str_num[i + 1:])
                right_trunc = int(str_num[:-i - 1])
                if not (is_prime(left_trunc) and is_prime(right_trunc)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)