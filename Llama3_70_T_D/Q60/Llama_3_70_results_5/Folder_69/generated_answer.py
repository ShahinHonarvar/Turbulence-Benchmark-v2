def is_prime(n):
    if n < 2:
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

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        if is_prime(num):
            left_truncatable = True
            right_truncatable = True
            for i in range(len(num_str) - 1):
                if not is_prime(int(num_str[i + 1:])):
                    left_truncatable = False
                    break
            for i in range(len(num_str) - 1):
                if not is_prime(int(num_str[:-i - 1])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes