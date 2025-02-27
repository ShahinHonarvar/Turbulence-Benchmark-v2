def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            left_truncated = True
            right_truncated = True
            for i in range(len(str_num) - 1):
                if not is_prime(int(str_num[i + 1:])):
                    left_truncated = False
                    break
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    right_truncated = False
                    break
            if left_truncated and right_truncated:
                left_right_truncatable_primes.append(num)
    single_digit_primes = [2, 3, 5, 7]
    for prime in single_digit_primes:
        if prime <= x:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)