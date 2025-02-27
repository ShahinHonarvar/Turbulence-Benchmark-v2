def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    truncatable_primes = []
    for num in range(11, x + 1):
        if is_prime(num) and '0' not in str(num):
            left_right_truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                left_trunc = int(str_num[i:])
                right_trunc = int(str_num[:-i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)