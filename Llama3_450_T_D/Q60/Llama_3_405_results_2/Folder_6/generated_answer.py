def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    truncatable_primes = set()
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            left_right_truncatable = True
            for i in range(len(str_num)):
                if len(str_num) - i > 1:
                    left_trunc = int(str_num[i:])
                    right_trunc = int(str_num[:-1 - i])
                    if not is_prime(left_trunc) or not is_prime(right_trunc):
                        left_right_truncatable = False
                        break
                else:
                    break
            if left_right_truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes))